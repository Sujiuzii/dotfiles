if status is-interactive
    # Commands to run in interactive sessions can go here
end

# disable greetings
set -g fish_greeting

# alias
thefuck --alias | source
