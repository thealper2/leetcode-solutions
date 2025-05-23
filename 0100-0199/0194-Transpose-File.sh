awk '
    { 
        for (i=1; i<=NF; i++) 
            a[i]= (a[i]? a[i] FS $i: $i) 
    } 
    END { 
        for (i in a) 
            print a[i] 
    }' file.txt
