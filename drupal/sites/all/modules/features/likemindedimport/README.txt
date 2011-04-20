This feature provides

To import our LikeMinded CouchDB, on another site, do the following.

1. Install this feature.
2. Create a new "LikemindedSource" content type page.
node/add/likemindedsource

3. Add this URL in the URL field (which points to our pheattle couchDB)

http://pheattle.iriscouch.com/likeminded_projects/_design/projects/_view/all

4. In JSONPATH PARSER SETTINGS

Provide the values to parse the JSON document.

context:
$.rows.*

field_problem
value.problem

field_process
value.process

field_result
value.result

title:
value.name

5. Updating the import.
As you add new fields, you can map categories, links and other features. 

Edit the feed:
admin/structure/feeds/edit/likeminded

Change the mapping:
admin/structure/feeds/edit/likeminded/mapping

Add a new source (JSONPath Expression) and map it to your field.



### Data
#### An Good Example of a Couch resource

From:
http://ec2-184-72-175-193.compute-1.amazonaws.com:5984/_utils/document.html?likeminded_projects/e73dafceef7641d4f860bb9f5d4044fa



### Mappings

#### Done
name (Title)
problem (Text: field_problem)
process (Text: field_process)
result (Text: field_result)

#### In progress

categories   category  [0]  (Taxonomy: Categories)
location  city (Taxonomy: City)

#### To do
start_date
end_date
resources   [0]  {id, name, description, url, created, updated, link}  (? Are there no pictures?)
status  {1, 2, ?}  (What do these values correspond to?)  (map to a select text field w/ values)
location {slug, zipcode, city, county, state_name, state_prefix, area_code, time_zone, lat, lon, is_free_text }
link
external_feed_account (?)
