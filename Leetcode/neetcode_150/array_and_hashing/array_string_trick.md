


# Array/String Tricks

- If the output is asked to be pair or subarray

```bash

             Array / String
               /      \
            Pair     Subarray
             |           |
          Sorted?     Only +ve nums?
           /   \         /       \
        Yes     No    Yes        No
        /        \     |          |
 Two Pointers  HashMap  Sliding   Prefix Sum
                         Window    + HashMap
                                      |
                                   (Kadane for max sum)


```