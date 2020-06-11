from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

class Dist_from_pdf(stats.rv_continuous):
	def __init__(self,pdf_in):
		super(Dist_from_pdf,self).__init__()
		self.pdf_in = pdf_in
	def _pdf(self,x):
		return self.pdf_in(x)


class Component_dist(stats.rv_continuous):
	def __init__(self,
	family_and_parameters,
	sign=1,
	truncate_left_of_mode=0,
	x_translation=0,
	):
		super(Component_dist,self).__init__()
		if family_and_parameters["family"] == 'normal':
			mu = family_and_parameters["parameters"]["mu"]
			sigma = family_and_parameters["parameters"]["sigma"]
			self.base = stats.norm(mu,sigma)
		

		self.transformed = Dist_from_pdf(lambda x: self.base.pdf(x*sign+x_translation))

class Mixture_dist(stats.rv_continuous):
	def __init__(self, dists_weights):
		super(Mixture_dist,self).__init__()
		self.dists_weights = dists_weights

	def _pdf(self, x):
		density = 0
		for component_dist in self.dists_weights:
			density += component_dist.pdf(x)*self.dists_weights[component_dist]
		density /= len(self.dists_weights)
		return density

dist1 = Component_dist(family_and_parameters = {
							'family' : 'normal',
							'parameters' : {'mu':3,'sigma':1}},
						sign = -1,
						truncate_left_of_mode = 0,
						x_translation = 0,
)

dist2 = Component_dist(family_and_parameters = {
							'family' :'normal',
							'parameters' : {'mu':3,'sigma':1}},
						sign = 1,
						truncate_left_of_mode = 0,
						x_translation = 0,
)

mixture = Mixture_dist({dist1.transformed:0.5,dist2.transformed:0.5})


x = np.linspace(-5,5,100)
fig, ax = plt.subplots()
ax.plot(x,mixture.pdf(x))
plt.show()