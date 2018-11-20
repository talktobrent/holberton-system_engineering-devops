#!/usr/bin/env ruby
puts ARGV[0].scan(/^([[:digit:]]{3}( |-){0,1}){2}[[:digit:]]{4}$/).join
