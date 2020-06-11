dist1 = {
	family_and_parameters = {
		family = ''
		parameters = {}
	}
	weight = 
	sign = 
	truncate_left_of_mode = 
	x_translation = 
}

class Component_dist(rv_continuous):
	def transform(dist,
	sign=1,
	truncate_left_of_mode=0,
	x_translation=0):
		dist = sign*dist
		dist = dist - x_translation 
		# todo: truncation
		return dist

	def __init__(self,
	family_and_parameters,
	sign=1,
	truncate_left_of_mode=0,
	x_translation=0,
	):
		if family_and_parameters["family"] == 'Normal':
			mu = family_and_parameters["parameters"]["mu"]
			sigma = family_and_parameters["parameters"]["sigma"]
			self.base = stats.norm(mu,sigma)
		self.sign=sign
		self.truncate_left_of_mode=truncate_left_of_mode
		self.x_translation=x_translation

		self.transformed = transform(self.base)

def Mixture_dist(rv_continuous):
    def __init__(self, dists_weights):
        super(mixture_dist).__init__()
        self.dists_weights = dists_weights

    def _pdf(self, x):
        for component_dist in self.dists_weights:
            pdf += component_dist.pdf(x)*dists_weights[component_dist]
        pdf /= len(self.dists_weights)
        return pdf

dist1 = Component_dist({
						family_and_parameters = {
							family = ''
							parameters = {}
						}
						sign = 1
						truncate_left_of_mode = 0
						x_translation = 0
}

dist2 = Component_dist({
						family_and_parameters = {
							family = ''
							parameters = {}
						}
						sign = 1
						truncate_left_of_mode = 0
						x_translation = 0
}

mixture = Mixture_dist({dist1:0.2,dist2:0.3})

