"""
Title: Graph API v1.0 Nested Data Leak Simulation
Author: Cybersecurity & Data Ethics Portfolio
Description: Demonstrates how legacy relational APIs (like Facebook Graph API v1.0) 
inadvertently leaked downstream node data without peer-level consent.
"""

# Mock database simulating how a graph database structures nested friend data
mock_social_graph = {
    "user_01": {
        "name": "Mansi", 
        "authorized_app": True, 
        "friends": ["user_02", "user_03"]
    },
    "user_02": {
        "name": "Nandika", 
        "authorized_app": False, 
        "location": "New York", 
        "psychographic_profile": "Highly Convincible / Neurotic"
    },
    "user_03": {
        "name": "Vanij", 
        "authorized_app": False, 
        "location": "Delhi", 
        "psychographic_profile": "Traditionalist / Resilient"
    }
}

def exploit_nested_api(target_user_id):
    print("=" * 60)
    print(f"CRITICAL SYSTEM TRAVERSAL: Simulating Graph API v1.0 Exploit")
    print("=" * 60)
    
    # 1. Verify if the primary user allowed the application
    if mock_social_graph[target_user_id]["authorized_app"]:
        print(f"[+] OAuth Token Generated for Primary User: {mock_social_graph[target_user_id]['name']}")
        print(f"[!] Accessing Social Edges via target node...")
        
        # 2. Extract the relational connections (social edges)
        friends_list = mock_social_graph[target_user_id]["friends"]
        
        print(f"[-] Discovered {len(friends_list)} downstream friend nodes linked to {mock_social_graph[target_user_id]['name']}.")
        print("\n=== STARTING RECURSIVE DATA HARVESTING (ZERO CONSENT) ===")
        
        # 3. Flaw: The system allows un-hashed data extraction of non-consenting users
        for friend_id in friends_list:
            friend_data = mock_social_graph[friend_id]
            print(f"\n[LEAKED NODE] ID: {friend_id}")
            print(f"  -> Name: {friend_data['name']}")
            print(f"  -> Location: {friend_data['location']}")
            print(f"  -> Target Metric: {friend_data['psychographic_profile']}")
            
        print("=" * 60)
        print("[SUCCESS] Data harvesting complete. Architectural boundary bypass successful.")
        print("=" * 60)
    else:
        print("[X] Access Denied. Primary user has not authenticated the app.")

if __name__ == "__main__":
    exploit_nested_api("user_01")
