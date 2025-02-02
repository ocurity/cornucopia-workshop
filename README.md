# Cornucopia Workshop

This repository contains the artifacts for delivering the workshop on how to Threat Model an example application using OWASP Cornucopia.

This workshop has been delivered to Defcon 31 AppSec Village and several private events.


## How to use

## Scenario

F-Corp just finished coding their brand new multitenanted "Anti-Fraud 2.0" application to be used by their customers in the Fintech space.
Customers and internal policy require a Threat Model before the application is allowed into production.
F-Corp arranged a meeting of your threat modeling team with the lead developer of the application so you can ask them questions and they can answer them. Your job is to document as many security considerations(good and bad) around the project as possible and maybe find a few high-impact issues along the way.

Due to the criticality of the application, deployments are done personally by the lead developer.
To deploy a new instance the developer personally builds a container locally and pushes it to the remote registry.

### Quick Version

Split participants into groups of 4. They are the threat modelers
Each group gets assigned a helper, helpers are the developers.
Developers have the code, the solutions and the "knowledge of the system" which means that they are running the session and they get a final say on what's going on.

At the beginning of the game each Threat Modeler gets 4 cards.

Each round they play the card that is most likely to create the most serious vulnerabilities.
After playing their individual card, each Threat Modeler takes  turns asking the developer questions related to the threats on their cards.
The developer either answers from the solutions or makes up an answer.

Each valid threat is 1 point, at the end of the round the person with most threats wins.

#### Example

A player has played: "Authorization Q" 
("Christopher can inject a command that the application will run at a higher privilege level")

The application suffers from a sqli, the application connects to the DB as admin and the DB IS a higher privilege level and unlimited access to it makes this threat valid.
This is a valid threat, the player is awarded 1 point.

#### Negative Example

A player has played: "Authorization 10" 
(Richard can bypass the centralized authorization controls since they are not being used comprehensively on all interactions")

The application does authorization by checking the provided API token against a list of hardcoded api tokens.
This is done as before the one request processed by the application is further processed.
It's not a valid threat.

Players might argue that the SQLI technically is a bypass of the tokens, but they are used comprehensively.


# Slides

https://docs.google.com/presentation/d/1q2W107TGjwDdWi90288kjHfPYWKYBzWvmywXhZCW6IM/edit#slide=id.g25d41d86f4d_0_69

