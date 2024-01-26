# 24accuracy.py by Pearce Pelia done

def performance(tp, fp, tn, fn):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1 = 2 * ((precision * recall) / (precision + recall))
	accuracy = (tp + tn) / (tp + fp +tn + fn)
	return f1, accuracy
	
print(performance(1,2,3,4))
print(performance(2,4,6,8))
print(performance(3,5,7,9))