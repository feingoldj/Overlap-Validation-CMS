import FWCore.ParameterSet.Config as cms

process = cms.Process("ReRec")

process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# pointing skim
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/187/00000/6A3231B8-DC76-E811-B7AD-FA163EAF8008.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/177/00000/40BD9C3D-CC76-E811-9D94-02163E01A074.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/176/00000/00615E28-C676-E811-80A3-FA163E2D8A7B.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/175/00000/4C35BC52-C376-E811-80D9-FA163E2CEAC7.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/174/00000/84F6EE15-C076-E811-878A-02163E019FCD.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/173/00000/D848A960-BF76-E811-8A4B-FA163E506ED2.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/172/00000/926E90A0-B876-E811-8ADB-FA163E88D3BA.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/170/00000/3E8C4F74-B676-E811-94F7-FA163EC40DE1.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/169/00000/F2062788-B576-E811-8CFB-FA163EA87350.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/168/00000/EE940B9F-B776-E811-B8AE-02163E019FE8.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/167/00000/34AC0BE5-B476-E811-BEA7-FA163E0C49C6.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/166/00000/FCFBED25-BB76-E811-A580-FA163EA3AA19.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/165/00000/5CA427DD-AD76-E811-8B31-FA163EF96F9B.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/164/00000/5C4A454F-B976-E811-9448-FA163E16E007.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/163/00000/DAE850B1-B176-E811-A278-02163E01A135.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/162/00000/FC04F4FC-9D76-E811-BA7B-FA163E081439.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/161/00000/40A66754-8976-E811-A252-02163E013E38.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/160/00000/0631C99D-7E76-E811-8D6A-FA163E3637B6.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/159/00000/F2C75603-8676-E811-B41D-FA163E7749C0.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/158/00000/D8B23CF3-8476-E811-92DF-FA163E434352.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/142/00000/C6B998A5-6D76-E811-B745-FA163E95BBB1.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/140/00000/7484B663-5076-E811-8F78-02163E01A03B.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/136/00000/84F95C5A-5676-E811-B865-FA163E57B0C7.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/133/00000/CC3F88E4-5376-E811-B9AF-FA163E83935C.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/129/00000/8C1EECC4-5776-E811-B3EC-FA163E42C086.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/118/00000/BA351727-5376-E811-9D65-02163E00C0D2.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/116/00000/E2FC706D-4176-E811-B3C8-02163E01A159.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/112/00000/1EBB1B5F-4B76-E811-8A95-FA163E9D9A3E.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/111/00000/2CC729EC-3176-E811-BE5A-FA163EDA7FBE.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/110/00000/60A2F517-2B76-E811-B6D9-FA163EB5D489.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/109/00000/A28A7DFA-2776-E811-BA49-FA163E0C9AD3.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/106/00000/8CEF0B15-2B76-E811-8E1D-FA163E39F017.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/101/00000/78BE7C94-2F76-E811-8865-FA163E1A9BF9.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/100/00000/FCCD746F-2376-E811-A3BB-FA163EC2BBB1.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/096/00000/862BC9B4-2476-E811-9E6C-FA163EB2E120.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/094/00000/FE283FE1-1B76-E811-816A-FA163ED07A21.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/091/00000/C401C0BF-1D76-E811-82F5-FA163EA6FD7C.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/090/00000/C825CEE3-1D76-E811-AA27-FA163EE6AFEB.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/089/00000/8076B3EA-1476-E811-8136-FA163EC0210C.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/087/00000/5C33DA24-1676-E811-85EE-FA163EA410A9.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/086/00000/7C2678CF-1476-E811-A38A-FA163E1DBA3E.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/085/00000/385193A3-1176-E811-BB1F-02163E00BCD9.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/083/00000/D266E093-1576-E811-AC92-FA163E0476F1.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/082/00000/C29E1BEB-1476-E811-B8B1-FA163E968D2C.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/079/00000/D66D620E-1D76-E811-B212-02163E015EB8.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/078/00000/1496D246-0E76-E811-AC43-FA163E1359B0.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/075/00000/24F18CEF-0D76-E811-B804-FA163EC6168E.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/071/00000/C07CBB29-0A76-E811-8D5A-FA163EFED7E2.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/069/00000/9A317AE3-0C76-E811-9E0B-FA163EE28A99.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/052/00000/4EDED7D0-FC75-E811-A139-FA163E9E07F9.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/051/00000/5A7ED516-0376-E811-A5ED-FA163E4D6DEF.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/050/00000/34CE5E28-F875-E811-854C-FA163E1A6759.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/049/00000/74B033A9-F375-E811-AA30-FA163E6E00CC.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/048/00000/C8F6EDD2-0176-E811-9B24-02163E013A67.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/047/00000/24130E81-FC75-E811-93D1-FA163E62D2D6.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/046/00000/02F972B4-F075-E811-96AD-FA163E396B84.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/045/00000/1CDA3C2F-DE75-E811-8067-FA163E0E9E08.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/044/00000/A650ACBC-B875-E811-8490-FA163E701E59.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/043/00000/E4A8D8EF-B375-E811-8946-FA163EE14499.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/042/00000/6C1F713A-9B75-E811-9532-FA163E5295CB.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/039/00000/0CD6A4E4-A275-E811-9748-FA163E7D8CF4.root",
"/store/data/Run2018B/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v2/000/318/038/00000/1086CC29-9B75-E811-AB73-FA163E054896.root",

    )
)

# output module#
#process.load("Configuration.EventContent.EventContentCosmics_cff")
#process.load("CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi")
#process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
#process.load("RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi")

# Conditions (Global Tag is used here):
#process.load("Configuration.Geometry.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '102X_dataRun2_TkAlSummerCamp_SG_v4'
#process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('TrackerAlignmentRcd'),
             tag = cms.string('Alignments'),
             connect = cms.string('sqlite_file:/afs/cern.ch/user/j/jfeingol/commonValidation/jfeingold/weakModes/test/neg_radial_readData.db'),
    ),
    cms.PSet(record = cms.string('SiPixelTemplateDBObjectRcd'),
             tag = cms.string('SiPixelTemplateDBObject_38T_TempForAlignmentReReco2018_v3'),
             connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    ),
)


#Geometry
#process.load("Configuration.StandardSequences.Geometry_cff")

# Real data raw to digi
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

# reconstruction sequence for Cosmics
#process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

# offline DQM
#process.load("DQMOffline.Configuration.DQMOfflineCosmics_cff")
#process.load("DQMServices.Components.MEtoEDMConverter_cff")

#L1 trigger validation
#process.load("L1Trigger.HardwareValidation.L1HardwareValidation_cff")
#process.load("L1Trigger.Configuration.L1Config_cff")
#process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFConfigProducer_cfi")
#process.load("L1TriggerConfig.CSCTFConfigProducers.L1MuCSCTFConfigurationRcdSrc_cfi")

#process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process, 'ALCARECOTkAlCosmicsCTF0T',
                                                     isPVValidation=False,
                                                     TTRHBuilder='WithAngleAndTemplate',
                                                     usePixelQualityFlag=True,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=True,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=False,
                                                     use_d0cut=False,
                                                    )





process.TFileService = cms.Service("TFileService",
    fileName = cms.string('Data_negRadial.root')
)

process.analysis = cms.EDAnalyzer("HitRes",
    usePXB = cms.bool(True),
    usePXF = cms.bool(True),
    useTIB = cms.bool(True),
    useTOB = cms.bool(True),
    useTID = cms.bool(True),
    useTEC = cms.bool(True),
    ROUList = cms.vstring('TrackerHitsTIBLowTof', 
        'TrackerHitsTIBHighTof', 
        'TrackerHitsTOBLowTof', 
        'TrackerHitsTOBHighTof'),
    trajectories = cms.InputTag("FinalTrackRefitter"),
    associatePixel = cms.bool(False),
    associateStrip = cms.bool(False),
    associateRecoTracks = cms.bool(False),
    tracks = cms.InputTag("FinalTrackRefitter"),
    barrelOnly = cms.bool(False)
)

# Path and EndPath definitions
process.p = cms.Path(process.seqTrackselRefit*process.analysis)
#process.endjob_step = cms.Path(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.p,process.endjob_step)
process.schedule = cms.Schedule(process.p)

