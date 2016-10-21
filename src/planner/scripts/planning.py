#!/usr/bin/env python

import re
import subprocess;
import os
import json
from os.path import expanduser 
from planningProperties import *
from generateProblem import updateProblem


script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

home_dir = expanduser("~");
finalPlanName = os.path.join(home_dir,'bestplan');


# createPlan(): invokes the planner and retrieve the new best plan
def createPlan():
    # perform the planning
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(["./plan"], stdout=FNULL, stderr=subprocess.STDOUT)

    # Identify the best plan found by the solver 
    last = "";
        
    for f in sorted([f for f in os.listdir(".") if "output" in f]):
        if len(last) > 0:
            os.remove(last);
        last = f;
    os.rename(last, finalPlanName)

def translatePlan():
    # If robot is currently performing a task, keep this in the plan, else empty the old plan
    for r in ROBOTS:
        plan[r] = [] if available[r] or len(plan[r]) == 0 else [plan[r][0]]

        finalPlanPath = finalPlanName

    webplan = []
    for i in DRONES:
        webplan.append({'name': 'Drone'+`i`, 'plan': ['Starting up']})
    for i in TURTLES:
        webplan.append({'name': 'Turtle'+`i`, 'plan': ['Starting up']})

    with open(finalPlanPath, 'r') as planFile:
        for line in planFile:
            m = re.findall(r"[\( ](\w+)", line)
            action = m[0];
            if action in ['pickup', 'putdown']:
                drone = int(m[1].strip('d'));
                crate = int(m[2].strip('c'));
                location = m[3];
                p = [action, crate, location];
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " Crate" + `crate` + " at location " + location)
            elif action in ['fly', 'drive']:
                agent = int(m[1].strip('d').strip('t'));
                destination = m[3];
                index = agent if (action == 'fly') else getTI(agent);
                p = [action, destination]
                addActionToPlan(index, p);
                if action == 'drive':
                    actions[len(actions)-1][2] = preceeding[agent]
                    preceeding[agent] = [];
                webplan[index]['plan'].append(p[0].title() + " to " + location)
            elif action in ['load', 'unload']:
                drone = int(m[1].strip('d'));
                crate = int(m[2].strip('c'));
                turtle = int(m[3].strip('t'));
                location = m[4];
                p = [action, crate, turtle, location];
                preceeding[turtle].append(len(actions));
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " Crate" + `crate` + " onto Turtle" + `turtle`)
            elif action in ['deliver']:
                drone = int(m[1].strip('d'));
                crate = int(m[2].strip('c'));
                type = int(m[3].strip('type'));
                person = int(m[4].strip('p'));
                location = m[5];
                p = [action, crate, type, person, location];
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " a crate of type " + `type` + " to " + `person`)

    for i in ROBOTS:
        webplan[i]['plan'].append("Finished");
    with open(home_dir + '/wasp_challenge_current_state', 'w') as f:
            json.dump(current, f)
    with open(home_dir + '/wasp_challenge_planning', 'w') as f:
        json.dump(webplan, f)

def addActionToPlan(robot, action):
    plan[robot].append(len(actions));
    actions.append([action, False, []]);

def cleanUp():
    # REMOVE CONSECUTIVE CANCELING ACTIONS:
    #    "fly to a then to b" becomes "fly to b"
    #    "pickup, then putdown" is removed
    for i in DRONES:
        p = plan[i];
        j = len(plan[i])-1;
        while j > 0:
            if actions[p[j]][0][0] == 'fly' and actions[p[j-1]][0][0] == 'fly':
                p.remove(p[j-1])
                j = len(plan[i])
            elif ((actions[p[j]][0][0] == 'putdown' and actions[p[j-1]][0][0] == 'pickup')
                or (actions[p[j]][0][0] == 'pickup' and actions[p[j-1]][0][0] == 'putdown' and actions[p[j]][0][1] == actions[p[j-1]][0][1])):
                p.remove(p[j])
                p.remove(p[j-1])
                j = len(plan[i])
            j -= 1

def printPlans():
    for i in ROBOTS:
        print "Plan of robot ",i; 
        for j in plan[i]: 
            print "\t",actions[j];



def updatePlan():
    createPlan();
    translatePlan();
    print "Plan Updated";

#updatePlan();

