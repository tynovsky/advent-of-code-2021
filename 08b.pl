#!/usr/bin/env perl

use strict;
use warnings;
use feature qw(signatures);
no warnings qw(experimental::signatures);
use List::Util qw(first);
use Data::Dumper;
use feature qw(say);

my $base_pattern = [
    'abcefg', 'cf', 'acdeg', 'acdfg',
    'bcdf', 'abdfg', 'abdefg', 'acf',
    'abcdefg', 'abcdfg'
];

sub apply_perm($digit_str, $perm) {
    my %translit;
    @translit{'a' .. 'g'} = split //, $perm;
    return join('', sort(split //, ($digit_str =~ s/(.)/$translit{$1}/gr)))
}
    
sub is_perm_valid($pattern, $perm) {
    my $perm_pattern = [ map { apply_perm($_, $perm) } @$pattern ];
    return join('', sort(@$perm_pattern)) eq join('', sort(@$base_pattern))
}

sub read_number($digit_str, $perm) {
    return first { $base_pattern->[$_] eq apply_perm($digit_str, $perm) } 0..9
}

sub perms($elements) {
    my $perms = [];
    my @elements = @$elements;
    return [$elements[0]] if @elements == 1;
    for my $i (0 .. $#elements) {
	$perms = [@$perms, map { $elements[$i] . $_ } @{perms([@elements[0 .. $i-1, $i+1 .. $#elements]])} ]
    }
    return $perms
}    

my $all_perms = perms(['a' .. 'g']);

my $sum = 0;

while (my $line = <>) {
    chomp($line);
    my ($signal_pattern, $four_digits) = map { [split / / ] } split / \| /, $line;

    for my $perm (@$all_perms) {
	# say $perm;
        if (is_perm_valid($signal_pattern, $perm)) {
            $sum += join '', map { read_number($_, $perm) } @$four_digits;
            last
    	}
    }
}

say $sum;
