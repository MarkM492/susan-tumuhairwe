# Local preview. Opening the HTML files directly (file://) blocks the self-hosted font in some browsers,
# so serve the site over http instead. Requires Python (py -3) on the PC.
Set-Location "$PSScriptRoot\site"
Write-Host "Preview at http://localhost:8080  (Ctrl+C to stop)"
py -3 -m http.server 8080
