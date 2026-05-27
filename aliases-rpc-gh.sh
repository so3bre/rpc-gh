# Service management commands
alias rpc-gh-start='systemctl --user start rpc-gh.service'
alias rpc-gh-stop='systemctl --user stop rpc-gh.service'
alias rpc-gh-status='systemctl --user status rpc-gh.service'
alias rpc-gh-restart='systemctl --user restart rpc-gh.service'

# Edit the service file using the full configuration
alias rpc-gh-edit='systemctl --user edit --full rpc-gh.service'

# View real-time service logs
alias rpc-gh-logs='journalctl --user -u rpc-gh.service -f'
