# how to interpret: [lower bound, upper bound, weight associated with the range lower bound to upper bound]
gapWeights = [[1,2, 0.2], [3,4, 0.5]]

def getBusyness(line_configuration, gapWeights):
	active_zones = 0
	for zone in line_configuration:
		if zone == 1:
			active_zones += 1
	
	gaps = find_gaps(line_configuration)
	for index, gap in enumerate(gaps):
		for lower_bound, upper_bound, weight in gapWeights:
			if lower_bound <= gap <= upper_bound:
				gaps[index] = weight
	return active_zones - sum(gaps)
	
def find_gaps(line_configuration):
	gaps = []
	gStart, gEnd = 0,0
	while gStart < len(line_configuration):
		gapFound = False
		if line_configuration[gStart] == 0:
			possibleGapLength = 0
			while gEnd < len(line_configuration) and line_configuration[gEnd] == 0:
				possibleGapLength += 1
				gEnd += 1
			if gEnd != len(line_configuration):
				gaps.append(possibleGapLength)
				gapFound = True
		if gapFound:
			gStart = gEnd
		else:
			gStart += 1
			gEnd = gStart
	return gaps
	

def tests():
	# the following tests test for correctness of busyness values and if the gaps were identified correctly
	# scx means sensor configuration x
	sc1 = [1,1,0,0,1,1]
	busyness_val = getBusyness(sc1, gapWeights)
	gaps = find_gaps(sc1)
	assert busyness_val == (4 - 0.2)
	validGapValue = True
	expectedGapValues = [2]
	for gap in gaps:
		if gap not in expectedGapValues:
			validGapValue &= False
	assert validGapValue == True
	print(f'TEST FOR CONFIGURATION {sc1} PASSED | WITH GIVEN GAP WEIGHTS: {gapWeights} BUSYNESS VALUE IS {busyness_val}')
	
	sc2 = [1,1,1,0,0,0,0]
	assert len(find_gaps(sc2)) == 0
	busyness_val = getBusyness(sc2, gapWeights)
	assert busyness_val == 3
	print(f'TEST FOR CONFIGURATION {sc2} PASSED | WITH GIVEN GAP WEIGHTS: {gapWeights} BUSYNESS VALUE IS {busyness_val}')
	
	sc3 = [0,0,1,0,0,1]
	busyness_val = getBusyness(sc3, gapWeights)
	gaps = find_gaps(sc3)
	assert busyness_val == (2 - 0.4)
	validGapValue = True
	expectedGapValues = [2, 2]
	for gap in gaps:
		if gap not in expectedGapValues:
			validGapValue &= False
	assert validGapValue == True
	print(f'TEST FOR CONFIGURATION {sc3} PASSED | WITH GIVEN GAP WEIGHTS: {gapWeights} BUSYNESS VALUE IS {busyness_val}')
	
	sc4 = [1,0,1,0,0,0, 1]
	busyness_val = getBusyness(sc4, gapWeights)
	gaps = find_gaps(sc4)
	assert busyness_val == (3 - 0.2 - 0.5)
	validGapValue = True
	expectedGapValues = [1, 3]
	for gap in gaps:
		if gap not in expectedGapValues:
			validGapValue &= False
	assert validGapValue == True
	print(f'TEST FOR CONFIGURATION {sc4} PASSED | WITH GIVEN GAP WEIGHTS: {gapWeights} BUSYNESS VALUE IS {busyness_val}')
	
	sc5 = [1,1,1,0,0,0,0,1]
	busyness_val = getBusyness(sc5, gapWeights)
	gaps = find_gaps(sc5)
	assert busyness_val == (4 - 0.5)
	validGapValue = True
	expectedGapValues = [4]
	for gap in gaps:
		if gap not in expectedGapValues:
			validGapValue &= False
	assert validGapValue == True
	print(f'TEST FOR CONFIGURATION {sc5} PASSED | WITH GIVEN GAP WEIGHTS: {gapWeights} BUSYNESS VALUE IS {busyness_val}')
	
	
	'''
	print(f'Busyness value: {getBusyness([1,1,0,0,1,1], gapWeights)}')
	print(f'Gaps: {find_gaps([1,0,0,0,0,1])}')
	print(f'Gaps: {find_gaps([1,0,1,0,0,1])}')
	print(f'Gaps: {find_gaps([1,1,1,0,0,1])}')
	print(f'Gaps: {find_gaps([0,0,1,0,0,1])}')
	'''

tests()

			
				
