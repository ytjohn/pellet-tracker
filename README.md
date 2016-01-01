Pellet Tracker
--------------

This is a simple application based off of django-rest-api. I need a simple application to track
how many bags of pellets I have in reserve, work out how many were consumed since the last update, and how
much I spent on pellets. This essentially relies on a human counting the bags and updating the "bags"
database model.

I also have a "hopper" model which relies on a sensor in the hopper that tracks how much is in the hopper 
itself.  To do this, I have a [particle.io photon](https://store.particle.io/collections/photon) connected to an
infrared light and photodiodes.  

"Bags" relies on manual counting, "Hopper" will be automatic. 

## Planned Features

Initial development is of the API. But in the future, I'd like to have:
 
 * human and mobile friendly forms to submit the hopper data
 * adding a filter by date range to the api
 * views showing graphs and tables over time
 * a comparison of consumption between hopper and bags model data
 * import weather data (mainly temperature and humidity) to contrast consumption data against the environment
 
  
