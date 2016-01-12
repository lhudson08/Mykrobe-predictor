MIN_CONF = -99999999
MIN_LLK = -99999999
class Typer(object):

	def __init__(self, depths, contamination_depths = [], error_rate = 0.05):
		self.depths = depths
		self.contamination_depths = contamination_depths
		self.error_rate = error_rate

	def type(self, l):
		raise NotImplemented("Implemented in sub class")

	def likelihoods_to_genotype(self, likelihoods, min_conf = MIN_CONF):
		ml = max(likelihoods)
		i = likelihoods.index(ml)
		if i == 0:
			if ml <= min_conf:
				gt = "-/-"
			else:
				gt = "0/0"
		elif i == 1:
			gt = "0/1"
		elif i == 2:
			gt = "1/1"
		return gt

	def has_contamination(self):
		return self.contamination_depths or len(self.depths) > 1		
