#!/usr/bin/env python3.8

users = [{ 'admin':False, 'active': False, 'name': 'Kevin'},
 { 'admin':True, 'active': False, 'name': 'Sandy'},
 { 'admin':False, 'active': False, 'name': 'Vesna'},
 { 'admin':False, 'active': False, 'name': 'Danny'},
 { 'admin':True, 'active': False, 'name': 'Christine'},
 { 'admin':False, 'active': True, 'name': 'Jessie'},
 { 'admin':True, 'active': True, 'name': 'Jack'},
 { 'admin':False, 'active': True, 'name': 'Gerald'},
 { 'admin':True, 'active': True, 'name': 'Gary'},
 { 'admin':True, 'active': False, 'name': 'Floyd'},
 { 'admin':True, 'active': False, 'name': 'Ned'},
 { 'admin':True, 'active': False, 'name': 'Bart'},
 { 'admin':True, 'active': False, 'name': 'Lisa'},
 { 'admin':False, 'active': False, 'name': 'Maggie'},
 { 'admin':False, 'active': True, 'name': 'Carl'},
 { 'admin':False, 'active': True, 'name': 'Tim'},
 { 'admin':True, 'active': True, 'name': 'Jose'},
 { 'admin':True, 'active': True, 'name': 'Tyrone'},
 { 'admin':True, 'active': True, 'name': 'Eric'}]

line_count = 0

for item in users:
    line_count += 1
    if item['active'] and item['admin']:
        print(f"{line_count}. ACTIVE - (ADMIN) {item['name']}")
    
    elif item['active']:
        print(f"{line_count}. ACTIVE - {item['name']}")

    elif item['admin']:
        print(f"{line_count}. (ADMIN) - {item['name']}")
    
    else:
        print(f"{line_count}. {item['name']}")
