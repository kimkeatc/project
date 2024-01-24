proc factorial {number} {
    set value 1
    for {set i 1} {$i <= $number} {incr i} {
        set value [expr {$value * $i}]
    }
    return $value
}
