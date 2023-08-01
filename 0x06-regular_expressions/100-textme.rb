#!/usr/bin/env ruby
# A Ruby script for output to have sender, receiver and flags.

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
