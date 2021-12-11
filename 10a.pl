#!/usr/bin/env perl

use strict;
use warnings;
use feature qw(say);
use Data::Dumper;

my %matching = ( '(' => ')', '[' => ']', '{' => '}',  '<' => '>');
my %penalty  = ( ')' => 3,   ']' => 57,  '}' => 1197, '>' => 25137, 'EOL' => 0);
my @res;
my $penalty = 0;
while (<>) {
	chomp;
	my @s;
	for my $c ((split //), "EOL") {
		# print @s, "\n";
		if ( grep {$_ eq $c} keys %matching ) {
			push @s, $c;
			next
		}
		my $e = $matching{(pop @s)};
		if ($e ne $c) {
			say "Expected $e, got $c instead.";
			$penalty += $penalty{$c};
			last
		}
	}
}

say $penalty;
