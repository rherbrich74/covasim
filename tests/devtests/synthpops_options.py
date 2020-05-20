'''
Script for testing integration with new SynthPops features -- namely, long-term
care facilities.
'''

import covasim as cv

which = ['simple', 'complex'][0]

if which == 'simple':

    sim = cv.Sim(pop_size=5000, pop_type='synthpops')
    popdict, layer_keys = cv.make_synthpop(sim, with_facilities=False, layer_mapping={'LTCF':'f'})
    sim.popdict = popdict
    sim.initialize()
    sim.run()


else:

    pars = dict(
        pop_size=20000,
        pop_type='synthpops',
        n_days=120,
        )

    sims = []
    for ltcf in [False, True]:
        print(f'Running LTCF {ltcf}')
        sim = cv.Sim(pars)
        popdict, layer_keys = cv.make_synthpop(sim, with_facilities=ltcf, layer_mapping={'LTCF':'f'})
        sim.popdict = popdict
        sim.reset_layer_pars(layer_keys)
        sims.append(sim)

    to_plot = ['cum_infections', 'new_infections', 'cum_severe', 'cum_deaths']
    msim = cv.MultiSim(sims)
    msim.run()
    msim.plot(to_plot=to_plot)
