import sys
import os
import argparse
import numpy as np

def entropy(vec, base=2):
	_, vec = np.unique(vec, return_counts=True)
	prob_vec = np.array(vec/float(sum(vec)))
	if base == 2:
		logfn = np.log2
	elif base == 10:
		logfn = np.log10
	else:
		logfn = np.log
	return prob_vec.dot(-logfn(prob_vec))

def conditional_entropy(x, y):
	uy, uyc = np.unique(y, return_counts=True)
	prob_uyc = uyc/float(sum(uyc))
	cond_entropy_x = np.array([entropy(x[y == v]) for v in uy])
	return prob_uyc.dot(cond_entropy_x)
	
def mutual_information(x, y):
	return entropy(x) - conditional_entropy(x, y)

def symmetrical_uncertainty(x, y):
	return 2.0*mutual_information(x, y)/(entropy(x) + entropy(y))

def getFirstElement(d):
	t = np.where(d[:,2]>0)[0]
	if len(t):
		return d[t[0],0], d[t[0],1], t[0]
	return None, None, None

def getNextElement(d, idx):
	t = np.where(d[:,2]>0)[0]
	t = t[t > idx]
	if len(t):
		return d[t[0],0], d[t[0],1], t[0]
	return None, None, None
	
def removeElement(d, idx):
	d[idx,2] = 0
	return d

def c_correlation(X, y):
	su = np.zeros(X.shape[1])
	for i in np.arange(X.shape[1]):
		su[i] = symmetrical_uncertainty(X[:,i], y)
	return su

def fcbf(X, y, thresh):
	n = X.shape[1]
	slist = np.zeros((n, 3))
	slist[:, -1] = 1
	slist[:,0] = c_correlation(X, y) 
	idx = slist[:,0].argsort()[::-1]
	slist = slist[idx, ]
	slist[:,1] = idx
	if thresh < 0:
		thresh = np.median(slist[-1,0])
		#print ("Using minimum SU value as default threshold: {0}".format(thresh))
	elif thresh >= 1 or thresh > max(slist[:,0]):
		print ("No relevant features selected for given threshold.")
		print ("Please lower the threshold and try again.")
		exit()
		
	slist = slist[slist[:,0]>thresh,:] 
	cache = {}
	m = len(slist)
	p_su, p, p_idx = getFirstElement(slist)
	for i in range(m):
		p = int(p)
		q_su, q, q_idx = getNextElement(slist, p_idx)
		if q:
			while q:
				q = int(q)
				if (p, q) in cache:
					pq_su = cache[(p,q)]
				else:
					pq_su = symmetrical_uncertainty(X[:,p], X[:,q])
					cache[(p,q)] = pq_su

				if pq_su >= q_su:
					slist = removeElement(slist, q_idx)
				q_su, q, q_idx = getNextElement(slist, q_idx)
				
		p_su, p, p_idx = getNextElement(slist, p_idx)
		if not p_idx:
			break
	
	sbest = slist[slist[:,2]>0, :2]
	return sbest

def fcbf_wrapper(inpath, thresh, delim=',', header=False, classAt=-1):
	if os.path.exists(inpath):
		try:
			if header:
				d = np.genfromtxt(inpath, delimiter=str(delim), skip_header=0)
			else:
				d = np.loadtxt(inpath, delimiter=delim)
			print ("Dimensions: {0} x {1}".format(d.shape[0], d.shape[1]))
		except Exception as e:
			print ("Error:", e)
			raise e
			exit()
		
		if classAt == -1:
			X = d[:, :d.shape[1]-1]
			y = d[:,-1]
		else:
			idx = np.arange(d.shape[1])
			X = d[:, idx[idx != classAt]]
			y = d[:, classAt]	

		try:
			print ('X: {}, y: {}'.format(X.shape, len(y)))
			sbest = fcbf(X, y, thresh)
			print ("\n#Features selected: {0}".format(len(sbest)))
			print ("Selected feature indices:\n{0}".format(sbest))
		except Exception as e:
			print ("Error:", e)			
	else:
		print ("The file you specified does not exist.")
	
def main():
	inpath = '../data/marutitma.csv'
	delim = ','
	thresh = -1 
	header = True
	classAt = -1 
	fcbf_wrapper(os.path.abspath(inpath), thresh, delim, header, classAt)
if __name__ == '__main__':
	if len(sys.argv) == 1:
		main()
	else:
		parser = argparse.ArgumentParser(description='Fast Correlation-Based Filter Selection (FCBF)')
		parser.add_argument('-inpath', metavar='', type=str, \
							dest='inpath', help='Path to input file')
		parser.add_argument('-thresh', metavar='', type=float, \
							dest='thresh', help='SU threshold')
		parser.add_argument('-delim', metavar='', type=str, \
							dest='delim',help='File delimiter', default=',')
		parser.add_argument('-header', metavar='', type=bool, \
							dest='header',help='Contains header?', default=False)
		parser.add_argument('-classAt', metavar='', type=int, \
							dest='classAt',help='Index of class column', default=-1)
							
		args = parser.parse_args()
		
		fcbf_wrapper(os.path.abspath(args.inpath), args.thresh, \
					args.delim.decode('string_escape'), args.header, args.classAt)
		
