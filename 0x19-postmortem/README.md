-- Postmortem example --
# Website downtime Postmortem (incident #001)

![alt text](https://github.com/adesekosamdev/alx-system_engineering-devops/blob/master/0x19-postmortem/postmortem.jpg)

## Date

2024-05-13

## Authors

* Samuel Tobi Adeseko

## Status

Complete

## Issue Summary

Duration: 3 hours, starting at 10:00 AM and ending at 1:00 PM (GMT)

## Impact

The user authentication service was intermittently unavailable, resulting in login failures for approximately 20% of users.

## Root Causes

The root cause of the issue was identified as a misconfiguration in the load balancer settings, causing an imbalance in traffic distribution to the authentication service instances.

![alt text](https://github.com/adesekosamdev/holberton-system_engineering-devops/blob/master/0x19-postmortem/meme-it-is-fine.jpg)

## Trigger

The load balancer went rogue, playing favorites among authentication service instances. Some were overloaded, while others were chilling with a cocktail on an empty beach.

## Resolution

We kindly reminded the load balancer of its duties and adjusted its settings to spread the love evenly among all instances.

## Detection

The monitor system installed on the servers sent an email.


## Timeline

2019-10-21 (*all times UTC*)

| Time     | Description |
| -------- | ----------- |
| 10:00 AM | Uh-oh! Monitoring alerts start screaming about increased error rates in the authentication service. Panic mode activated! |
| 10:05 AM | Engineering team receives a wakeup call and jumps into action. |
| 10:15 AM | **INCIDENT BEGINS** Initial investigation begins, but it's like finding a needle in a haystack.|
| 10:30 AM | We blame the database! Classic move, right?  |
![alt text](https://github.com/HeimerR/holberton-system_engineering-devops/blob/master/0x19-postmortem/500error.jpg)
| 10:45 AM | The network operations team is called in for backup.|

| 11:00 AM | Load balancer settings under scrutiny. Somebody had a bad day configuring those. |
| 11:30 AM | **OUTAGE ENDS** Adjustments made, load balanced back to being as happy as a clam. |
| 1:00 PM | **INCIDENT ENDS** Service stability restored, and we're feeling like superheroes! |

## Corrective and preventative measures
Lessons Learned

 	Single points of failure are the biggest risk

* Monitoring quickly alerted us to a high rate (reaching ~100%) of HTTP 500s
* Rapidly was set up a temporary configuration

Action Items

| Action Item | Type | Owner | Bug |
| ----------- | ---- | ----- | --- |
| We're installing a "Load Balancer Whisperer" to keep an eye on it 24/7. |
| Adding a big red button labeled "Panic Mode" for emergency situations. **TODO** |
| Task: Host a load balancer appreciation day with cake and balloons to maintain good relations. **TODO** |
| Planning a team-building session to improve communication between load balancers and services. | **TODO** |
| Task: Implement load balancer configuration audits every fortnight to prevent any more shenanigans. **TODO** |
