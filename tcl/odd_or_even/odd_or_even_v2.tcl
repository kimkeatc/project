proc is_even {number} {
    return [expr {($number & 1) == 0} ? true : false]
}

proc is_odd {number} {
    return [expr {($number & 1) == 1} ? true : false]
}
