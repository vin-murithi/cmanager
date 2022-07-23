#get affiliate level
def get_affiliate_level(recruitor_id):
    #split recruitor id
    recruitor_affiliate_level = recruitor_id.split('-')
    #take the first section of Id
    recruitor_affiliate_level = recruitor_affiliate_level[0]
    #increment id and return it
    recruitee_affiliate_level = chr(ord(recruitor_affiliate_level)+1)
    return recruitee_affiliate_level

get_affiliate_level()