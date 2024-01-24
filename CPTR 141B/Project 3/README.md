# CPTR 141: Project #3

## Problem Overview
Imagine you are a contestant on a game show and before you are three doors. $10,000 in cash has randomly been placed behind one door. Behind the other two doors are the consolation prizes of dishwasher detergent. The game show host asks you to select a door, and you randomly pick one. However, before revealing the prize behind your door, the game show host reveals one of the other doors that contains a consolation prize. At this point, the game show host asks if you would like to stick with your original choice or to switch to the remaining door. What do you choose?

Write a program to allow the user play the game repeatedly. Keep track of the number of times the user stayed with the original choice and the number of times the user switched to the alternate door. For each choice, keep track of the win/loss ratio and report the results when the user choses to stop playing.

As an alternative to playing the game directly, allow the user to simulate the game show problem a selected number of times. Your function should randomly select locations for the prizes, select a door at random chosen by the contestant, and then randomly choose to either stay with the original choice or switch to the alternate door. As before, keep track of the win/loss ratio and report the results when the user choses to stop playing.

## Solution Specification
Your solution should strive to meet the standards specified below as they form the basis on which it will be graded.

1. Your program must prompt the user for input in a meaningful way and check for possible error conditions.
2. Have the user enter a seed for the random number generator so that your runs are repeatable.
3. Since this is a project, you have a lot of freedom in how you choose to accomplish the task.  However, you are expected to make use of the following concepts somewhere in your program.

    * Appropriately named variables
    * Computation (addition, multiplication, division, etc.)
    * At least one Boolean expression
    * At least one branching statement (``if``, ``else``, and/or ``elif``)
    * At least one iteration statement (``while`` and/or ``for``)
    * At least one function is defined and used in your program

## Hints

### Door to Reveal

The game starts with the prize being placed (at random) behind one of three doors and the user picking one of three doors (at random in the simulation). Next, your program needs to pick a door to reveal. We can think of this selection process as starting at some door and going through the doors till we find one that (a) does not have the prize and (b) is not the user's selection. 

Our search could always start with the first door, and since this may be easier to code, you can start there. The problem with this search algorithm is that if you reveal door 3, the user can assume that the prize is behind the door that they didn't select (otherwise your search algorithm would have picked an earlier door). So it would be better to start the search at a random place, but that means that we need to support wrapping. 

I suggest that you write a function `otherDoorFrom(doorA, doorB);` that returns a (randomly-selected) door that is different from either of the parameters (who can be equal to each other).

### Sample

A compiled example program is available to try. Note that you do not need to match the user interaction exactly; creativity is encouraged. Right-click the project directory, select ``Open in Terminal``, and type:

```
python3 gameShowExample.pyc
```

## Code Review and Grading
Before you can receive an ``M`` on your project, you must participate in a [code review](https://en.wikipedia.org/wiki/Code_review) with someone who has taken CPTR 242--for example, a CS tutor at the Student Development Center.  This walk-through style review is a guided-tour of your source code in which you describe how you implemented the various features, explain why you made the choices you did, and solicit constructive input which might help improve your final product.  Turn in the signed form to your instructor.

Once your final product has been turned in, it will be graded according to the following rubric.

<style>
  #grade td, #grade th {
    padding: 2px;
    border: 1px solid black;
  }
</style>
<table id="grade" cellspacing="0">
  <tr>
    <th style="width: 5%"></th>
    <th style="width: 23.75%">Algorithm</th>
    <th style="width: 23.75%">User Interaction</th>
    <th style="width: 23.75%">Use of Required Concepts</th>
    <th style="width: 23.75%">Coding Style</th>
  </tr>
  <tr>
    <th>E</th>
    <td>Handles both a live user game and a set of simulated games</td>
    <td>Excellently formatted output and handles input errors well</td>
    <td>All required concepts included</td>
    <td>Code is well commented and readable</td>
  </tr>
  <tr>
    <th>M</th>
    <td>Handles a live user game or a set of simulated games but not both</td>
    <td>Good formatting and handles most input errors</td>
    <td>All required concepts included</td>
    <td>Code is sparsely commented or over-commented but mostly readable</td>
  </tr>
  <tr>
    <th>R</th>
    <td>An attempt to implement the game was made, but was not successful</td>
    <td>Basic user interaction with little or no input validation</td>
    <td>Some required concepts were used, but not all</td>
    <td>Comments are sparse or non-existent and the code is very hard to follow</td>
  </tr>
  <tr>
    <th>N</th>
    <td>No attempt at implementing the game is evident</td>
    <td>No user interaction or input validation</td>
    <td>Only one or two required concepts were included</td>
    <td>Comments are lacking and/or code is unreadable</td>
  </tr>
</table>