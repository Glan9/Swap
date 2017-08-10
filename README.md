# Swap

Swap is a 2D, self-modifying esolang. The IP (instruction pointer) starts in the top left initially moving right. The IP wraps around when it goes out of bounds.

Sounds pretty normal? The catch is that after stepping over a command, it swaps to an "opposite" command.

## Commands

### Movement

    >    Make the IP start moving right
    <    Make the IP start moving left
    ^    Make the IP start moving up
    v    Make the IP start moving down
    \    Mirror: Swap horizontal and vertical directions
    /    Mirror: Swap and invert horizontal and vertical directions
    |    Mirror: Turn around if moving horizontally
    _    Mirror: Turn around if moving vertically
    [    If moving right, go left
    ]    If moving left, go right
    ?    Pop a value. Jump over the next command if that value is 0
    !    Pop a value. Jump over the next command if the value is not 0
    x    End execution

### Stack

    "    Toggle string mode. While in string mode, every character stepped over is pushed to the stack (as codepoint)
    '    Push the next character stepped over to the stack
    0-9  Number literals, push that number
    i    Read a character from input and push its codepoint
    o    Pop and print (as character)
    ,    Duplicate top of stack
    .    Delete top of stack
    %    Toggle the active stack
    $    Swap the top two stack elements
    @    Put the top stack element on the bottom
    #    Put the bottom stack element on top

### Calculation

    +    Pop the top two, push their sum
    -    Pop the top two, push their difference
    *    Pop the top two, push their product
    :    Pop the top two, push their quotient (integer division)
    (    Pop top two, push 1 if second < first else 0
    )    Pop top two, push 1 if second > first else 0
    =    Pop top two, push 1 if equal else 0
    ~    Pop top two, push 1 if not equal else 0

## Swapping

Below are the pairs of opposite commands that get swapped with each other:

    <> v^ /\ |_ [] ?! sx "' io ,. %$ @# +- *: () =~
    
Note that `s` is a no-op but gets switched anyway.
