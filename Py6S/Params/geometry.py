import solar
import dateutil.parser

class Geometry:
  class User:
    """Stores parameters for a user-defined geometry for 6S.
    
    Attributes:
    
     * ``solar_z`` -- Solar zenith angle
     * ``solar_a`` -- Solar azimuth angle
     * ``view_z`` -- View zenith angle
     * ``view_a`` -- View azimuth angle
     * ``day`` -- The day the image was acquired in (1-31)
     * ``month`` -- The month the image was acquired in (0-12)
    
    """
    
    solar_z = 0
    solar_a = 0
    view_z = 0
    view_a = 0
    day = 1
    month = 1
    
    def __str__(self):
      return '0 (User defined)\n%d %d %d %d %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day)
      
    def from_time_and_location(self, lat, long, datetimestring, view_z, view_a):
      """Sets the user-defined geometry to a given view zenith and azimuth, and a solar zenith and azimuth calculated from the lat, long and date given.
      
      Uses the PySolar module for the calculations
      
      """
      dt = dateutil.parser.parse(datetimestring, dayfirst=True)
      self.solar_z = solar.GetAltitude(lat, long, dt)
      
      az = solar.GetAzimuth(lat, long, dt)
      
      if az < 0:
        self.solar_a = abs(az) + 180
      else:
        self.solar_a = abs(az - 180)
        
      self.solar_a = solar_a % 360
      
      self.day = dt.day
      self.month = dt.month
      
      self.view_z = view_z
      self.view_a = view_a
      
      
    
  class Meteosat:
    """Stores parameters for a Meteosat geometry for 6S.
    
    Attributes:
    
      * ``month`` -- The month the image was acquired in (0-12)
      * ``day`` -- The day the image was acquired in (1-31)
      * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
      * ``column`` -- The Meteosat column of the image
      * ``line`` -- The Meteosat line of the image
    
    """
    
    
    month = 1
    day = 1
    gmt_decimal_hour = 0
    column = 0
    line = 0
    
    def __str__(self):
      return '1 (Meteosat)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
      
  class GoesEast:
    """Stores parameters for a GOES East geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
     * ``column`` -- The GOES East column of the image
     * ``line`` -- The GOES East line of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    column = 0
    line = 0
    
    def __str__(self):
      return '2 (Goes East)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
      
      
  class GoesWest:
    """Stores parameters for a GOES West geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
     * ``column`` -- The GOES West column of the image
     * ``line`` -- The GOES West line of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    column = 0
    line = 0
    
    def __str__(self):
      return '3 (Goes West)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
      
  class AVHRR_PM:
    """Stores parameters for a AVHRR afternoon pass geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``column`` -- The AVHRR column of the image
     * ``ascendant_node_longitude`` -- The longitude of the ascendant node of the image
     * ``ascendant_node_hour`` -- The hour of the ascendant node of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    column = 0
    ascendant_node_longitude = 0
    ascendant_node_hour = 0
    
    def __str__(self):
      return '4 (AVHRR PM NOAA)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)
      
  class AVHRR_AM:
    """Stores parameters for a AVHRR morning pass geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``column`` -- The AVHRR column of the image
     * ``ascendant_node_longitude`` -- The longitude of the ascendant node of the image
     * ``ascendant_node_hour`` -- The hour of the ascendant node of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    column = 0
    ascendant_node_longitude = 0
    ascendant_node_hour = 0
    
    def __str__(self):
      return '5 (AVHRR AM NOAA)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)
      
  class SPOT_HRV:
    """Stores parameters for a SPOT HRV geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
     * ``latitude`` -- The latitude of the centre of the image
     * ``longitude`` -- The longitude of the centre of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    longitude = 0
    latitude = 0
    
    def __str__(self):
      return '6 (SPOT)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)
      
  class Landsat_TM:
    """Stores parameters for a Landsat TM geometry for 6S.
    
    Attributes:
    
     * ``month`` -- The month the image was acquired in (0-12)
     * ``day`` -- The day the image was acquired in (1-31)
     * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
     * ``latitude`` -- The latitude of the centre of the image
     * ``longitude`` -- The longitude of the centre of the image
    
    """
    month = 1
    day = 1
    gmt_decimal_hour = 0
    longitude = 0
    latitude = 0
    
    def __str__(self):
      return '7 (TM)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)