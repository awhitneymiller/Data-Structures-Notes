Classes: object-oriented programming
    Functional:
        * outputs are a function of inputs and nothing else
        * no external variables that modify what's going on in it.

    Object Oriented
        * Outputs are a function of inputs and some other factors maintained in a state

State:
    *the values of some variables of interest that are maintained for the program to perform necessary record-keeping.

Functional:
    Gist : Organizes flow of a program as a stateless sequence of function calls, without side-effects between each.
        ex: Calls to the abs(num) function, which returns the absolute value of num, or pow(base,ep) function, which returns base^exp
        abs(-19) => 19
        pow(2, 3) => 8.0
    * Calls to pow() or abs() do not affect each other, no state is carried over from one call to next.


Object Oriented:
    Gist : Organizes flow of a program as a stateful sequence of commands to objects, preserving state between each.
        ex: Designing a video game player that has some health, which can be doubled with the doubleHealth() method.
        player.health => 10
        player.doubleHealth(); // player.health now 20
        player.doubleHealth(); // player.health now 40
    *Commands to the player object in the form of doubleHealth() depend on its current state in player.health;

- review using (self)

Saalmon
    two types right now:
    burnymon -> "fire-type"
    dampymon -> "water-type"
saalmon have names

Behaviors:
    Taking damage of a certain time
        * dampymon take 5 burns damage from burnymon attacks
    burnymon -> 15 health
    dampymon -> 25 health

when "printing" a Saalmon they will repeat their name 2 times
