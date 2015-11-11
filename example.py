from traceroute import Traceroute
trt = Traceroute("8.8.8.8", source="sources/sources.json")
hops = trt.traceroute()

for h in hops:
    print "Hop: ", h
