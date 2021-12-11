#!/usr/bin/env perl

use strict;
use warnings;
use feature qw(say);
use Data::Dumper;

my %matching = ( '(' => ')', '[' => ']', '{' => '}',  '<' => '>');
my %pointval = ( '(' => 1  , '[' => 2  , '{' => 3  ,  '<' => 4  );
my @res;
my $penalty = 0;
my @scores;
while (<>) {
	chomp;
	my @s;
	for my $c ((split //), "EOL") {
		# print @s, "\n";
		if ( grep {$_ eq $c} keys %matching ) {
			push @s, $c;
			next
		}
		my $p = pop @s;
		my $e = $matching{$p};
		if ($e ne $c) {
			say "Expected $e, got $c instead.";
			if ($c eq "EOL") {
				push @s, $p;
				my $score = 0;
				while (@s) {
					my $b = pop @s;
					$score = 5*$score + $pointval{$b};
				}
				push @scores, $score;
			}
			last
		}
	}
}

@scores = sort {$a <=> $b} @scores;
say $scores[(scalar(@scores) - 1)/2];
