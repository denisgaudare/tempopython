import dask.config
dask.config.set({"cloudprovider.digitalocean.token": "yourAPItoken"})
import dask_cloudprovider.digitalocean
cluster = DropletCluster(n_workers=1)