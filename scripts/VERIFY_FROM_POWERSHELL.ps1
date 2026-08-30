$ErrorActionPreference = 'Stop'

Write-Host '=== K=3 GAUSSIAN BAI SOFT-FREEZE EXACT AUDIT ==='

$repoRoot = Split-Path -Parent $PSScriptRoot
$script = Join-Path $repoRoot 'src\verify_soft_freeze.py'

if (-not (Test-Path -LiteralPath $script)) {
    throw "Audit script not found: $script"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw 'Python was not found on PATH.'
}

$exe = $python.Source
if ($python.Name -eq 'py.exe' -or $python.Name -eq 'py') {
    $prefix = @('-3')
} else {
    $prefix = @()
}

$version = & $exe @prefix -c "import sympy; print(sympy.__version__)"
if ($LASTEXITCODE -ne 0) {
    throw 'Could not import SymPy.'
}
if ($version.Trim() -ne '1.14.0') {
    throw "Expected SymPy 1.14.0, found $($version.Trim()). Install with: python -m pip install -r requirements.txt"
}

$output = & $exe @prefix $script 2>&1
$output | ForEach-Object { Write-Host $_ }
if ($LASTEXITCODE -ne 0) {
    throw "Symbolic audit exited with code $LASTEXITCODE"
}

$text = ($output | Out-String)
if ($text -notmatch 'PASS_EXACT_SYMBOLIC_AUDIT') {
    throw 'Missing PASS_EXACT_SYMBOLIC_AUDIT marker.'
}
if ($text -notmatch 'BERNSTEIN_INTERVALS_PASS = 5/5') {
    throw 'Missing BERNSTEIN_INTERVALS_PASS = 5/5 marker.'
}

Write-Host 'PASS_RELEASE_REPRODUCTION_GATE'
