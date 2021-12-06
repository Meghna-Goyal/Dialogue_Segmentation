# Dialoguen Segmentation Using Maximum Entropy Approach.

Detect critical changes in flow of human-machine interaction (Dialogue Segmentation) using Maximum Entropy Approach.

### Input Corpus Description:

1. Corpus of child-robot interaction.
2. 36 recorded sessions, with the total duration of 222 minutes.
3. Each session divided into 2 parts:
      Introduction
      Robot instructs the child to perform therapy relevant exercises.
4. Robot Roles: command, question, statement, and offer.
5. Child: correct/partial/incorrect response or no response.

### Code Description:

* To detect the critical change, we performed two experiments
    * Single segmentation breakpoint: Find a single breakpoint in the Dialouge Segement with maximum overall entropy of the two parts of the segment.
      ```bash
      python ./SingleBreakPoint_Max_Entropy.py
      ```
    * Two segmentation breakpoints: Find a multiple breakpoint in the Dialouge Segement with maximum overall entropy of the multiple parts of the segment.
     ```bash
     python ./MultiBreakPoint_Max_Entropy.py
     ```
    * Plot the Graphs of the Entropy:
      ```bash
     python ./SingleBreakPoint_Max_Entropy_plot.py
      ```

    








