import FWCore.ParameterSet.Config as cms

process = cms.Process("ReRec")

process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# pointing skim
'/store/mc/RunIISpring18CosmicDR/TKCosmics_38T/ALCARECO/TkAlCosmics0T-DECO_100X_mc2017cosmics_realistic_deco_v3-v1/30000/0287153A-753B-E811-9DDA-0CC47A4DEDFE.root'
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
process.GlobalTag.globaltag = '100X_upgrade2018_design_IdealBS_v8'
#process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('TrackerAlignmentRcd'),
             tag = cms.string('Alignments'),
             connect = cms.string('sqlite_file:radialTest.db')
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
    fileName = cms.string('HitResRadial1.root')
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

