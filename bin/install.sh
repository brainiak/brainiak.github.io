#!/usr/bin/env bash

# Assume MacOS

which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
    brew update
fi

brew install node

# Install RVM
curl -L get.rvm.io | bash -s stable
mkdir ~/.local/lib
rvm install ruby --latest
rvm use --latest --default

npm install -g gulp
npm install

gem install bundle
bundle install
