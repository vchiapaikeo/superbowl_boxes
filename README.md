# superbowl_boxes
Randomly generates superbowl boxes for you and your friends.

# CLI Test
(superbowl_boxes) vchiapaikeo-mbp:superbowl_boxes vchiapaikeo$ python3 generate_boxes.py --friends="Victor, Garrett, Ryan, Nina, Carmen, Jon"

2018-02-03 16:23:49,871 - __main__ - INFO - List of friends passed: ['Victor', 'Garrett', 'Ryan', 'Nina', 'Carmen', 'Jon']
2018-02-03 16:23:49,871 - __main__ - INFO - Final Results: 
1: Carmen 2: Nina 3: Ryan 4: Ryan 5: Nina 6: Victor 7: Garrett 8: Garrett 9: Garrett 10: Ryan 
11: Ryan 12: Carmen 13: Nina 14: Jon 15: Carmen 16: Victor 17: Victor 18: Carmen 19: Nina 20: Victor 
21: Jon 22: Nina 23: Nina 24: Victor 25: Garrett 26: Victor 27: Ryan 28: Carmen 29: Ryan 30: Carmen 
31: Nina 32: Nina 33: Victor 34: Nina 35: Garrett 36: Victor 37: Carmen 38: Victor 39: Garrett 40: Ryan 
41: Victor 42: Jon 43: Carmen 44: Jon 45: Carmen 46: Garrett 47: Victor 48: Ryan 49: Carmen 50: Jon 
51: Garrett 52: Jon 53: Nina 54: Victor 55: Victor 56: Ryan 57: Ryan 58: Jon 59: Garrett 60: Ryan 
61: Garrett 62: Nina 63: Nina 64: Victor 65: Ryan 66: Nina 67: Jon 68: Nina 69: Garrett 70: Carmen 
71: Carmen 72: Garrett 73: Victor 74: Carmen 75: Carmen 76: Victor 77: Victor 78: Nina 79: Jon 80: Ryan 
81: Nina 82: Carmen 83: Victor 84: Carmen 85: Victor 86: Garrett 87: Nina 88: Carmen 89: Garrett 90: Ryan 
91: Victor 92: Nina 93: Jon 94: Garrett 95: Jon 96: Victor 97: Victor 98: Carmen 99: Carmen 100: Carmen 

# Flask test
(superbowl_boxes) vchiapaikeo-mbp:superbowl_boxes vchiapaikeo$ flask run
 * Serving Flask app "server"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2018-02-03 17:00:17,611 - app.generate - INFO - Final Results: 
1: Ryan 2: Garrett 3: Paulo 4: Ephraim 5: Jay K 6: Victor 7: Victor 8: Jay K 9: Ephraim 10: Ryan 
11: Ryan 12: Paulo 13: Jay Ly 14: Jay K 15: Christian 16: Garrett 17: Jay K 18: Christian 19: Paulo 20: Ryan 
21: Paulo 22: Victor 23: Paulo 24: Victor 25: Carmen 26: Paulo 27: Jay K 28: Jay K 29: Christian 30: Ryan 
31: Paulo 32: Victor 33: Garrett 34: Ephraim 35: Ephraim 36: Ephraim 37: Jay Ly 38: Victor 39: Carmen 40: Carmen 
41: Jay Ly 42: Carmen 43: Jay K 44: Victor 45: Jay Ly 46: Christian 47: Nina 48: Garrett 49: Paulo 50: Jon 
51: Ryan 52: Christian 53: Jon 54: Jay Ly 55: Jon 56: Victor 57: Christian 58: Jay Ly 59: Victor 60: Carmen 
61: Garrett 62: Ryan 63: Jon 64: Ephraim 65: Jay K 66: Victor 67: Carmen 68: Garrett 69: Victor 70: Jon 
71: Paulo 72: Ephraim 73: Paulo 74: Ryan 75: Jay K 76: Jon 77: Ryan 78: Victor 79: Victor 80: Victor 
81: Jon 82: Jay Ly 83: Christian 84: Christian 85: Jay K 86: Victor 87: Jon 88: Christian 89: Christian 90: Jay Ly 
91: Carmen 92: Carmen 93: Ryan 94: Ryan 95: Ryan 96: Jay Ly 97: Jay K 98: Nina 99: Jay K 100: Christian 

127.0.0.1 - - [03/Feb/2018 17:00:17] "GET / HTTP/1.1" 200 -
