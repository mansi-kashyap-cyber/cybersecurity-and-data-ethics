# Technical Post-Mortem: Nested Relational Vulnerabilities in Facebook's Graph API v1.0

This case study maps out the architectural flaws within Facebook's early data-graph models that allowed third-party applications to harvest massive datasets without direct user consent.

## 🛠️ The Architectural Flaw: Graph API Over-Privileging

The core vulnerability was not an external exploit, database injection, or malicious payload. It was a structural design flaw within the **Facebook Graph API (v1.0)** architecture.

### The Mechanism of the Leak
Facebook’s data backend models social networks as a property graph containing **Nodes** (Users, Pages) and **Edges** (Relationships, Friends). When a user authenticated a third-party app (such as the "thisisyourdigitallife" quiz), they granted an OAuth 2.0 access token. 

However, under Graph API v1.0, this access token didn't just authorize access to the user's personal node; it automatically extended read permissions across the user’s **social edges**. Because the API lacked boundary constraints, querying `/me/friends` returned not just the unique IDs of their connections, but nested data payloads (likes, locations, birthdays) of those friends—despite those friends having never interacted with the app.

#### 💻 Simulation Script

To illustrate how open API endpoints inadvertently leak nested relational data when data-graph access controls are poorly designed, I wrote a Python simulation script.

*   See the code file: [`api_leak_simulation.py`](./api_leak_simulation.py)

##### How to Run the Simulation
```bash
python api_leak_simulation.py
```

###### 💡 Engineering Safeguards
1.  **Strict Node-Level Authorization:** Access tokens must validate authorizations for *every single node* retrieved in a query graph, rather than relying on the parent node's permissions.
2.  **Context-Aware Fields:** API endpoints must explicitly strip nested child-object arrays unless explicitly requested and verified via multi-party authorization loops.


