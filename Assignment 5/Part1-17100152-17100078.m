%function [T] = gridWorld
clc;
clear;
close all;

% Grid world layout:
%gridWorld
%  --------------------------
%  |  1 |  2 |  3 |  4 |  5 |
%  --------------------------
%  |  6 |  7 |  8 |  9 | 10 |
%  --------------------------
%  | 11 | 12 | 13 | 14 | 15 |
%  --------------------------
%  | 16 | 17 | 18 | 19 | 20 |
%  --------------------------
%  | 21 | 22 | 23 | 24 | 25 |
%  --------------------------
%
%  Start state: 6
%  Goal state: 25
%  Bad state: 5 && 21
%  End state: 26
%
%  The end state is an absorbing state that the agent transitions
%  to after visiting the goal state.
%
%  There are 17 states in total (including the end state)
%  and 4 actions (up, down, right, left).
%

%%%%%%%%%%%%%%%%%%% rewards %%%%%%%%%%%%%%%%%%%%%%

% Rewards are stored in a one dimensional array R(s)
%
% All states have a reward of -1 except:
% Goal state: 100
% Bad state: -70
% End state: 0

% initialize rewards to -1
R = -ones(26,1);

% set rewards
R(25) = 100;  % goal state
R(5) = -70;  % bad state
R(21) = -70; % bad state
R(26) = 0;    % end state

%%%%%%%%%%%%%%%%%% transitions %%%%%%%%%%%%%%%%%%%

% Transitions are stored in a 3 dimensional array T(s,s',a) such that
% T(s,s',a) = Pr(s'|s,a)
% You can store transition probabilities in your own way. This is just 
% to help you understand the various transitions and probabilities
% Make sure you adjust your probabilities according to the obstacles.

% initialize all transition probabilities to 0
T = zeros(25,25,4);


% setting goal, end and start state
startState = 1;
goalState = 25;
endState = 26;

% For a given action, the agent has probability 0.8 of moving
% by one square in the intended direction and probability 0.1
% of moving sideways.  When the agent bumps into a wall,
% it stays in its current location.

% transition parameters
% a = 0.9;  % intended move
% b = 0.05;  % lateral move

a = 0.8; % intended move
b = 0.1; % lateral move

% up (a = 1)   

T(1,1,1) = a+b;
T(1,2,1) = b;

T(2,1,1) = b;
T(2,2,1) = a+b;

T(3,2,1) = b;
T(3,3,1) = a;
T(3,4,1) = b;

T(4,3,1) = b;
T(4,4,1) = a;
T(4,5,1) = b;

T(5,4,1) = b;
T(5,5,1) = a+b;

T(6,6,1) = b;
T(6,1,1) = a;
T(6,7,1) = b;

T(7,6,1) = b;
T(7,2,1) = a;
T(7,8,1) = b;

T(8,7,1) = b;
T(8,3,1) = a;
T(8,9,1) = b;

T(9,8,1) = b;
T(9,4,1) = a;
T(9,9,1) = b;

T(10,9,1) = b;
T(10,5,1) = a;
T(10,10,1) = b;

T(11,11,1) = b;
T(11,6,1) = a;
T(11,12,1) = b;

T(12,11,1) = b;
T(12,7,1) = a;
T(12,13,1) = b;

T(13,12,1) = b;
T(13,8,1) = a;
T(13,13,1) = b;

T(14,14,1) = a+b;
T(14,15,1) = b;

T(15,14,1) = b;
T(15,10,1) = a;
T(15,15,1) = b;

T(16,16,1) = a+b;
T(16,17,1) = b;

T(17,17,1) = 1;

T(18,13,1) = a+b;
T(18,19,1) = b;

T(19,18,1) = b;
T(19,19,1) = a;
T(19,20,1) = b;

T(20,19,1) = b;
T(20,15,1) = a;
T(20,20,1) = b;

T(21,21,1) = b;
T(21,16,1) = a;
T(21,22,1) = b;

T(22,21,1) = b;
T(22,17,1) = a;
T(22,23,1) = b;

T(23,22,1) = b;
T(23,18,1) = a;
T(23,24,1) = b;

T(24,23,1) = b;
T(24,19,1) = a;
T(24,25,1) = b;

T(25,25,1) = 1;
T(25,26,1) = 1;

% down (a = 2)

T(1,1,2) = b;
T(1,6,2) = a;
T(1,2,2) = b;

T(2,1,2) = b;
T(2,6,2) = a;
T(2,2,2) = b;

T(3,3,2) = b;
T(3,8,2) = a;
T(3,4,2) = b;

T(4,3,2) = b;
T(4,9,2) = a;
T(4,5,2) = b;

T(5,4,2) = b;
T(5,10,2) = a;
T(5,5,2) = b;

T(6,6,2) = b;
T(6,11,2) = a;
T(6,7,2) = b;

T(7,6,2) = b;
T(7,12,2) = a;
T(7,8,2) = b;

T(8,7,2) = b;
T(8,13,2) = a;
T(8,8,2) = b;

T(9,9,2) = a+b;
T(9,10,2) = b;

T(10,9,2) = b;
T(10,15,2) = a;
T(10,10,2) = b;

T(11,11,2) = a+b;
T(11,12,2) = b;

T(12,11,2) = b;
T(12,12,2) = a;
T(12,13,2) = b;

T(13,12,2) = b;
T(13,18,2) = a;
T(13,14,2) = b;

T(14,14,2) = a+b;
T(14,15,2) = b;

T(15,14,2) = b;
T(15,20,2) = a;
T(15,15,2) = b;

T(16,16,2) = b;
T(16,21,2) = a;
T(16,17,2) = b;

T(17,16,2) = b;
T(17,22,2) = a;
T(17,17,2) = b;

T(18,18,2) = b;
T(18,23,2) = a;
T(18,19,2) = b;

T(19,18,2) = b;
T(19,24,2) = a;
T(19,20,2) = b;

T(20,19,2) = b;
T(20,25,2) = a;
T(20,20,2) = b;

T(21,21,2) = a+b;
T(21,22,2) = b;

T(22,21,2) = b;
T(22,22,2) = a;
T(22,23,2) = b;

T(23,22,2) = b;
T(23,23,2) = a;
T(23,24,2) = b;

T(24,23,2) = b;
T(24,24,2) = a;
T(24,25,2) = b;

T(25,26,2) = 1;
T(26,26,2) = 1;

% left (a = 3)

T(1,1,3) = a+b;
T(1,6,3) = b;

T(2,2,3) = b;
T(2,1,3) = a;
T(2,7,3) = b;

T(3,3,3) = a+b;
T(3,8,3) = b;

T(4,4,3) = b;
T(4,3,3) = a;
T(4,9,3) = b;

T(5,5,3) = b;
T(5,4,3) = a;
T(5,10,3) = b;

T(6,1,3) = b;
T(6,6,3) = a;
T(6,11,3) = b;

T(7,2,3) = b;
T(7,6,3) = a;
T(7,12,3) = b;

T(8,3,3) = b;
T(8,7,3) = a;
T(8,13,3) = b;

T(9,4,3) = b;
T(9,8,3) = a;
T(9,9,3) = b;

T(10,5,3) = b;
T(10,9,3) = a;
T(10,15,3) = b;

T(11,6,3) = b;
T(11,11,3) = a+b;

T(12,7,3) = b;
T(12,11,3) = a;
T(12,12,3) = b;

T(13,8,3) = b;
T(13,12,3) = a;
T(13,18,3) = b;

T(14,14,3) = 1;

T(15,10,3) = b;
T(15,14,3) = a;
T(15,20,3) = b;

T(16,16,3) = a+b;
T(16,21,3) = a;

T(17,17,3) = b;
T(17,16,3) = a;
T(17,22,3) = b;

T(18,13,3) = b;
T(18,18,3) = a;
T(18,23,3) = b;

T(19,19,3) = b;
T(19,18,3) = a;
T(19,24,3) = b;

T(20,15,3) = b;
T(20,19,3) = a;
T(20,25,3) = b;

T(21,16,3) = b;
T(21,21,3) = a+b;

T(22,17,3) = b;
T(22,21,3) = a;
T(22,22,3) = b;

T(23,18,3) = b;
T(23,23,3) = a;
T(23,23,3) = b;

T(24,19,3) = b;
T(24,23,3) = a;
T(24,24,3) = b;

T(25,26,3) = 1;
T(26,26,3) = 1;

% right (a = 4)

T(1,1,4) = b;
T(1,2,4) = a;
T(1,6,4) = b;

T(2,2,4) = a+b;
T(2,7,4) = b;

T(3,3,4) = b;
T(3,4,4) = a;
T(3,8,4) = b;

T(4,4,4) = b;
T(4,5,4) = a;
T(4,9,4) = b;

T(5,5,4) = a+b;
T(5,9,4) = b;

T(6,1,4) = b;
T(6,7,4) = a;
T(6,11,4) = b;

T(7,2,4) = b;
T(7,8,4) = a;
T(7,12,4) = b;

T(8,3,4) = b;
T(8,9,4) = a;
T(8,13,4) = b;

T(9,4,4) = b;
T(9,10,4) = a;
T(9,9,4) = b;

T(10,5,4) = b;
T(10,10,4) = a;
T(10,15,4) = b;

T(11,6,4) = b;
T(11,12,4) = a;
T(11,11,4) = b;

T(12,7,4) = b;
T(12,13,4) = a;
T(12,12,4) = b;

T(13,8,4) = b;
T(13,13,4) = a;
T(13,18,4) = b;

T(14,14,4) = b+b;
T(14,15,4) = a;

T(15,10,4) = b;
T(15,15,4) = a;
T(15,20,4) = b;

T(16,16,4) = b;
T(16,17,4) = a;
T(16,21,4) = b;

T(17,17,4) = a+b;
T(17,22,4) = b;

T(18,13,4) = b;
T(18,19,4) = a;
T(18,23,4) = b;

T(19,19,4) = b;
T(19,20,4) = a;
T(19,24,4) = b;

T(20,15,4) = b;
T(20,20,4) = a;
T(20,25,4) = b;

T(21,16,4) = a;
T(21,22,4) = b;
T(21,21,4) = a;

T(22,17,4) = b;
T(22,23,4) = a;
T(22,22,4) = b;

T(23,18,4) = b;
T(23,24,4) = a;
T(23,23,4) = b;

T(24,19,4) = b;
T(24,25,4) = a;
T(24,24,4) = b;

T(25,26,4) = 1;
T(26,26,4) = 1;

discount = 0.99;

utilityp=zeros(25,1);
utilityn=zeros(25,1);

utilityn(25)=100;
utilityp(25)=100;

utilityn(5)=-70;
utilityp(5)=-70;


utilityn(21)=-70;
utilityp(21)=-70;

action_result=0;
finish=false;

while finish==false   
    for i=25:-1:1
        if(i==25 || i==5 || i==21)
           continue;
        end
        best_value=-inf;
        for action=1:4
            temp=0;
            for successor=25:-1:1                
                temp=temp+T(i,successor,action)*utilityp(successor);
            end 
            if temp>best_value
                best_value=temp;
            end        
        end
        utilityn(i)=R(i)+discount*best_value;     
    end
    check=abs(utilityn-utilityp) < 0.01;
    if (all(check==1))
        finish=true;
    end    
    utilityp=utilityn;
end;
policy=zeros(25,1);

for i=25:-1:1
    best_value=-inf;
    best_action=0;
    if(i==25 || i==5 || i==21)
       continue;
    end
    for action=1:4
        temp=0;
        for succ=25:-1:1                
            temp=temp+T(i,succ,action)*utilityp(succ);
        end
        if temp>best_value
               best_action=action;
        end
    end
    policy(i)=best_action;
end

% Write your code here





