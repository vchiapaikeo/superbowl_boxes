# superbowl_boxes
Randomly generates superbowl boxes for you and your friends.

## CLI Test
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

## Flask Test
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

## Py3 Test
(superbowl_boxes) vchiapaikeo-mbp:superbowl_boxes vchiapaikeo$ python3 app.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 2018-02-03 18:03:58,753 - server.generate - INFO - Final Results: 
 1: Ephraim 2: Jon 3: Paulo 4: Garrett 5: Ephraim 6: Jay Ly 7: Jay Ly 8: Nina 9: Victor 10: Jay K 
 11: Ryan 12: Ephraim 13: Jon 14: Victor 15: Jay Ly 16: Jay K 17: Paulo 18: Garrett 19: Ephraim 20: Victor 
 21: Nina 22: Carmen 23: Victor 24: Ryan 25: Paulo 26: Garrett 27: Garrett 28: Jay Ly 29: Garrett 30: Jon 
 31: Christian 32: Jay K 33: Carmen 34: Jay Ly 35: Jay Ly 36: Garrett 37: Christian 38: Carmen 39: Jay K 40: Carmen 
 41: Nina 42: Christian 43: Christian 44: Garrett 45: Carmen 46: Ryan 47: Carmen 48: Victor 49: Christian 50: Christian 
 51: Ryan 52: Victor 53: Jon 54: Nina 55: Ryan 56: Ryan 57: Paulo 58: Jon 59: Jay K 60: Ryan 
 61: Paulo 62: Christian 63: Jay K 64: Jay K 65: Ephraim 66: Jay K 67: Nina 68: Jon 69: Christian 70: Paulo 
 71: Ephraim 72: Jay Ly 73: Jon 74: Nina 75: Nina 76: Victor 77: Garrett 78: Paulo 79: Victor 80: Ephraim 
 81: Paulo 82: Victor 83: Christian 84: Ephraim 85: Nina 86: Paulo 87: Carmen 88: Jay Ly 89: Victor 90: Garrett 
 91: Jay K 92: Jon 93: Ephraim 94: Jon 95: Nina 96: Jay Ly 97: Ryan 98: Carmen 99: Carmen 100: Ryan 

 127.0.0.1 - - [03/Feb/2018 18:03:58] "GET / HTTP/1.1" 200 -

## Unit Test
```
[superbowl_boxes (master)]> pytest -v test/
============================================================= test session starts ==============================================================
platform darwin -- Python 3.6.5, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/vchiapaikeo/my-development/superbowl_boxes/venv/bin/python3.6
cachedir: .pytest_cache
rootdir: /Users/vchiapaikeo/my-development/superbowl_boxes
collected 2 items                                                                                                                              

test/test_generate.py::TestGenerate::test_gen_results PASSED                                                                             [ 50%]
test/test_generate.py::TestGenerate::test_get_random_names PASSED                                                                        [100%]

============================================================== 2 passed in 0.16s ===============================================================
```
