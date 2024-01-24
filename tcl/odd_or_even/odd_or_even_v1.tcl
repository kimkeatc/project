proc is_even {number} {
    return [expr {($number % 2) == 0} ? true : false]
}

proc is_odd {number} {
    return [expr {($number % 2) == 1} ? true : false]
}
