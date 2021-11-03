all: grid strata network
	

grid:
	../../src/cpp/build_grid.exe ./params/build_grid_params.in ./output/grid/leicestershire

strata:
	../../src/cpp/build_strata.exe ./params/build_strata_params.in ./output/grid/leicestershire ./output/strata/leicestershire

network:
	for i in 0 1 2 3 4; do \
		echo ../../src/cpp/build_network.exe ./params/build_network_params.in ./output/grid/leicestershire ./output/strata/leicestershire_group_distribution_$$i.hex ./output/networks/leicestershire_$$i; \
		../../src/cpp/build_network.exe ./params/build_network_params.in ./output/grid/leicestershire ./output/strata/leicestershire_group_distribution_$$i.hex ./output/networks/leicestershire_$$i; \
	done

seedIteration:
	for i in `seq 4`; do \
		echo $$i; \
		make clean; \
		echo python3 ./params/paramBuilder.py intSeed=$$i; \
		python3 ./params/paramBuilder.py intSeed=$$i; \
		make all ; \
		mkdir ./output_all/varSeed_leicestershire/$$i; \
		mkdir ./output_all/varSeed_leicestershire/$$i/params; \
		cp -r ./output/ ./output_all/varSeed_leicestershire/$$i; \
		mv ./params/*.in ./output_all/varSeed_leicestershire/$$i/params; \
	done

sizeIteration:
	for i in `seq 1 16`; do \
		mkdir ./output_all/varSize/$$i;\
		for j in `seq 4`; do\
			echo $$i $$j; \
			make clean; \
			echo $$(($$i*10000));\
			python3 ./params/paramBuilder.py intSeed=$$j intNoNodes=$$(($$i*10000)) intMCMCMaxSamplesInMillions=256; \
			make all ; \
			mkdir ./output_all/varSize/$$i/$$j;\
			mkdir ./output_all/varSize/$$i/$$j/params;\
			cp -r ./output/ ./output_all/varSize/$$i/$$j; \
			mv ./params/*.in  ./output_all/varSize/$$i/$$j/params; \
		done; \
	done

clean:
	#rm -r output/networks/*
	find output/networks/ -maxdepth 1 -type f -delete
	find output/grid/ -maxdepth 1 -type f -delete
	find output/strata/ -maxdepth 1 -type f -delete
