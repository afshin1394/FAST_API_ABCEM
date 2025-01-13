

class AreAllLocationsWithInDistanceServiceImpl(GetGISService):


        async def execute(self,) -> bool:
                  return  await self.repository.are_all_locations_within_distance()

