import networkit as nk

G = nk.readGraph("./input/karate.graph", nk.Format.METIS)
communities = nk.community.detectCommunities(G)
plmCommunities = nk.community.detectCommunities(G, algo=nk.community.PLM(G, True))
print("{0} elements assigned to {1} subsets".format(plmCommunities.numberOfElements(),
                                                    plmCommunities.numberOfSubsets()))

print(plmCommunities.getSubsets())
nk.community.writeCommunitiesNestedFormat(plmCommunities, "output/communtiesPLM.partition")