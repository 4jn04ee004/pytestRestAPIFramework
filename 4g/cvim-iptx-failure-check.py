import json

data = {
   "id":"site-management",
   "data":"{\"data\":{\"connectivityDetails\":[{\"torPort\":\"1\",\"siteCode\":\"klgce\",\"poTorDeploymentType\":\"TYPE1\",\"siteName\":\"kibapodgc14\",\"torType\":\"NR_TOR\",\"siteClusterId\":\"klgce1\",\"deploymentProfile\":\"Non-Mandatory\",\"technology\":\"4G\",\"torGroupID\":\"1\"}],\"siteInformation\":{\"address\":\"奈良県橿原市曽我町１１２５番１\",\"latitude\":\"34.51571389\",\"technology\":\"4G\",\"referenceId\":\"RNE2901000210\",\"zipcode\":\"634-0831\",\"stage\":\"Active\",\"propertyName\":\"\",\"solutionSubType\":\"RIU\",\"id\":\"4796cd3b-590b-444c-be54-0a0b6277f64d\",\"solutionType\":\"CRAN\",\"siteType\":\"Standard\",\"longitude\":\"135.7701769\",\"status\":\"Active\"}},\"eventType\":\"SITE_LOCATION_UPDATE_EVENT\",\"source\":\"\",\"operation\":\"MIGRATION\"}",
   "time":"1703676789632",
   "type":"event",
   "source":"site-management",
   "contentType":"application/json",
   "specVersion":"1.0",
   "traceParent":"temp"
}

dt = json.loads(data["data"])
new_dt = dt["data"]
print(new_dt)

pd = [
   {
      "sarfId":"RNE2901000210",
      "latitude":34.51571389,
      "longitude":135.7701769,
      "cellName":"RNE2901000210_10",
      "frequencyBand":"Band 3 - 20MHz",
      "technology":"LTE_FDD",
      "rdcCode":"yu2s4",
      "cdcCode":"TotsukaCDC",
      "bandwidth":"20MHz",
      "siteType":"OUTDOOR",
      "region":"KINKI",
      "prefecture":"29_NARA",
      "city":"KASHIHARA-SHI",
      "subRegion":"320_OSAKA",
      "areaCategory":"UR",
      "tac":30722,
      "height":14.8,
      "azimuth":130,
      "antennaName":None,
      "cellId":10,
      "pci":239,
      "zeroCorrelationZone":"9",
      "vduId":"2",
      "vcuId":"4",
      "siteRdcMapping":"",
      "siteGnbIdMapping":"",
      "rsi":"75",
      "gcCode":"ymkw2",
      "cuupId":"",
      "cucpId":"",
      "neighbourLteAnchor":"",
      "ruId":"10",
      "prachConfigIndex":0,
      "ulGrpAssmtPusch":"0",
      "ulPuschCycShiftCell":"0",
      "riuId":"4",
      "tiFlag":"",
      "tiDate":"",
      "leasedFlag":"",
      "mimoPath":"",
      "redT":"0",
      "rrhNum":"4",
      "txType":"Intra-network (Server and Interferer)",
      "mcc":0,
      "mnc":0,
      "downlinkArfcn":1500,
      "enodebId":None,
      "gnodebId":None,
      "siteUid":"",
      "active":"TRUE",
      "rfCluster":"NAR-KASHIHARASHI-SOUTH",
      "siteStatus":"12_On Air",
      "siteTypeClass":"Macro",
      "cityCode":"29205",
      "cityJpn":"橿原市",
      "eirp":"",
      "mTilt":0.0,
      "eTilt":5.0
   },
   {
      "sarfId":"RNE2901000210",
      "latitude":34.51571389,
      "longitude":135.7701769,
      "cellName":"RNE2901000210_11",
      "frequencyBand":"Band 3 - 20MHz",
      "technology":"LTE_FDD",
      "rdcCode":"yu2s4",
      "cdcCode":"TotsukaCDC",
      "bandwidth":"20MHz",
      "siteType":"OUTDOOR",
      "region":"KINKI",
      "prefecture":"29_NARA",
      "city":"KASHIHARA-SHI",
      "subRegion":"320_OSAKA",
      "areaCategory":"UR",
      "tac":30722,
      "height":14.8,
      "azimuth":240,
      "antennaName":None,
      "cellId":11,
      "pci":331,
      "zeroCorrelationZone":"9",
      "vduId":"2",
      "vcuId":"4",
      "siteRdcMapping":"",
      "siteGnbIdMapping":"",
      "rsi":"55",
      "gcCode":"ymkw2",
      "cuupId":"",
      "cucpId":"",
      "neighbourLteAnchor":"",
      "ruId":"11",
      "prachConfigIndex":0,
      "ulGrpAssmtPusch":"0",
      "ulPuschCycShiftCell":"0",
      "riuId":"5",
      "tiFlag":"",
      "tiDate":"",
      "leasedFlag":"",
      "mimoPath":"",
      "redT":"0",
      "rrhNum":"5",
      "txType":"Intra-network (Server and Interferer)",
      "mcc":0,
      "mnc":0,
      "downlinkArfcn":1500,
      "enodebId":None,
      "gnodebId":None,
      "siteUid":"",
      "active":"TRUE",
      "rfCluster":"NAR-KASHIHARASHI-SOUTH",
      "siteStatus":"12_On Air",
      "siteTypeClass":"Macro",
      "cityCode":"29205",
      "cityJpn":"橿原市",
      "eirp":"",
      "mTilt":0.0,
      "eTilt":3.0
   },
   {
      "sarfId":"RNE2901000210",
      "latitude":34.51571389,
      "longitude":135.7701769,
      "cellName":"RNE2901000210_12",
      "frequencyBand":"Band 3 - 20MHz",
      "technology":"LTE_FDD",
      "rdcCode":"yu2s4",
      "cdcCode":"TotsukaCDC",
      "bandwidth":"20MHz",
      "siteType":"OUTDOOR",
      "region":"KINKI",
      "prefecture":"29_NARA",
      "city":"KASHIHARA-SHI",
      "subRegion":"320_OSAKA",
      "areaCategory":"UR",
      "tac":30722,
      "height":14.8,
      "azimuth":350,
      "antennaName":None,
      "cellId":12,
      "pci":132,
      "zeroCorrelationZone":"9",
      "vduId":"2",
      "vcuId":"4",
      "siteRdcMapping":"",
      "siteGnbIdMapping":"",
      "rsi":"90",
      "gcCode":"ymkw2",
      "cuupId":"",
      "cucpId":"",
      "neighbourLteAnchor":"",
      "ruId":"12",
      "prachConfigIndex":0,
      "ulGrpAssmtPusch":"0",
      "ulPuschCycShiftCell":"0",
      "riuId":"6",
      "tiFlag":"",
      "tiDate":"",
      "leasedFlag":"",
      "mimoPath":"",
      "redT":"0",
      "rrhNum":"6",
      "txType":"Intra-network (Server and Interferer)",
      "mcc":0,
      "mnc":0,
      "downlinkArfcn":1500,
      "enodebId":None,
      "gnodebId":None,
      "siteUid":"",
      "active":"TRUE",
      "rfCluster":"NAR-KASHIHARASHI-SOUTH",
      "siteStatus":"12_On Air",
      "siteTypeClass":"Macro",
      "cityCode":"29205",
      "cityJpn":"橿原市",
      "eirp":"",
      "mTilt":2.0,
      "eTilt":5.0
   }
]

