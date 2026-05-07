import { defineConfig } from 'vitepress'
import { tabsMarkdownPlugin } from 'vitepress-plugin-tabs'

const rtdVersion = process.env.READTHEDOCS_VERSION
const rtdLanguage = process.env.READTHEDOCS_LANGUAGE || 'en'
const docsBase = rtdVersion ? `/${rtdLanguage}/${rtdVersion}/` : '/'

const logoPath = `${docsBase}androidaps-logo.png`
const faviconIcoPath = `${docsBase}favicon.ico`

export default defineConfig({
  base: docsBase,
  title: 'AndroidAPS Wiki',
  description: 'AndroidAPS documentation',
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: logoPath }],
    ['link', { rel: 'shortcut icon', href: faviconIcoPath }],
  ],
  cleanUrls: false,
  markdown: {
    config: (md) => {
      md.use(tabsMarkdownPlugin)
    },
  },
  themeConfig: {
    logo: logoPath,
    nav: [
      { text: 'Home', link: '/' },
    ],
    sidebar: [
      {
        text: `<img src="${logoPath}" alt="AAPS" style="max-width:100%; padding: 0.5rem 0;">`,
        link: '/',
        items: [],
      },
      {
        text: '1) Change language',
        items: [
          { text: 'Change language', link: '/NavigateDoc/ChangeLanguage' },
          { text: 'Change version', link: '/NavigateDoc/ChangeVersion' },
        ],
      },
      {
        text: '2) Getting started',
        items: [
          { text: 'Introduction to AAPS', link: '/Getting-Started/Introduction' },
          { text: 'Preparing for AAPS', link: '/Getting-Started/PreparingForAaps' },
          { text: 'Component Overview', link: '/Getting-Started/ComponentOverview' },
          { text: '- Compatible pumps', link: '/Getting-Started/CompatiblePumps' },
          { text: '- Compatible CGMs', link: '/Getting-Started/CompatiblesCgms' },
          { text: '- Compatible phones', link: '/Getting-Started/Phones' },
          { text: '- Compatible watches', link: '/Getting-Started/Watches' },
        ],
      },
      {
        text: '3) Setting up AAPS',
        items: [
          { text: 'Setting up the reporting server', link: '/SettingUpAaps/SettingUpTheReportingServer' },
          { text: '- Nightscout', link: '/SettingUpAaps/Nightscout' },
          { text: '- Tidepool', link: '/SettingUpAaps/Tidepool' },
          { text: 'Building AAPS', link: '/SettingUpAaps/BuildingAaps' },
          { text: '- Browser Build', link: '/SettingUpAaps/BrowserBuild' },
          { text: '- Android Studio Build', link: '/SettingUpAaps/ComputerBuild' },
          { text: '- CLI Build', link: '/SettingUpAaps/CLIBuild' },
          { text: 'Transferring and Installing AAPS', link: '/SettingUpAaps/TransferringAndInstallingAaps' },
          { text: 'Setup Wizard', link: '/SettingUpAaps/SetupWizard' },
          { text: 'Your AAPS Profile', link: '/SettingUpAaps/YourAapsProfile' },
          { text: 'Change AAPS configuration', link: '/SettingUpAaps/ChangeAapsConfiguration' },
          { text: '- Config Builder', link: '/SettingUpAaps/ConfigBuilder' },
          { text: '- Preferences', link: '/SettingUpAaps/Preferences' },
          { text: 'Completing the objectives', link: '/SettingUpAaps/CompletingTheObjectives' },
        ],
      },
      {
        text: '4) Daily Life with AAPS',
        items: [
          { text: 'AAPS Screens', link: '/DailyLifeWithAaps/AapsScreens' },
          { text: 'Key AAPS Features', link: '/DailyLifeWithAaps/KeyAapsFeatures' },
          { text: 'COB calculation', link: '/DailyLifeWithAaps/CobCalculation' },
          { text: 'Sensitivity detection', link: '/DailyLifeWithAaps/SensitivityDetectionAndCob' },
          { text: 'Profile Switch & Profile Percentage', link: '/DailyLifeWithAaps/ProfileSwitch-ProfilePercentage' },
          { text: 'Temp-Targets', link: '/DailyLifeWithAaps/TempTargets' },
          { text: 'Extended carbs', link: '/DailyLifeWithAaps/ExtendedCarbs' },
          { text: 'Automations', link: '/DailyLifeWithAaps/Automations' },
          { text: 'Dynamic ISF', link: '/DailyLifeWithAaps/DynamicISF' },
          { text: 'AAPS for children', link: '/DailyLifeWithAaps/AapsForChildren' },
          { text: 'Pumps and cannulas', link: '/DailyLifeWithAaps/PumpsAndCannulas' },
          { text: 'Timezone traveling & Daylight Saving Time', link: '/DailyLifeWithAaps/TimezoneTraveling-DaylightSavingTime' },
        ],
      },
      {
        text: '5) Remote AAPS features',
        items: [
          { text: 'Remote monitoring', link: '/RemoteFeatures/RemoteMonitoring' },
          { text: 'Remote control', link: '/RemoteFeatures/RemoteControl' },
          { text: 'SMS Commands', link: '/RemoteFeatures/SMSCommands' },
          { text: 'Following Only', link: '/RemoteFeatures/FollowingOnly' },
          { text: 'Android Auto', link: '/RemoteFeatures/AndroidAuto' },
        ],
      },
      {
        text: '6) Wear OS Smartwatches',
        items: [
          { text: 'AAPS for Wear OS', link: '/WearOS/BuildingAapsWearOS' },
          { text: 'Use the smartwatch', link: '/WearOS/WearOsSmartwatch' },
          { text: 'Remote control', link: '/RemoteFeatures/RemoteControlWearOS' },
          { text: 'Custom watchfaces reference', link: '/ExchangeSiteCustomWatchfaces/CustomWatchfaceReference' },
          { text: 'Exchange site custom watchfaces', link: '/ExchangeSiteCustomWatchfaces/' },
        ],
      },
      {
        text: '7) Maintenance of AAPS',
        items: [
          { text: 'Export/Import Settings', link: '/Maintenance/ExportImportSettings' },
          { text: 'Reviewing your data', link: '/Maintenance/Reviewing' },
          { text: 'AAPS Release Notes', link: '/Maintenance/ReleaseNotes' },
          { text: 'Documentation updates', link: '/Maintenance/DocumentationUpdate' },
          { text: 'Updating to a new version of AAPS', link: '/Maintenance/UpdateToNewVersion' },
          { text: '- Browser Update', link: '/Maintenance/UpdateBrowserBuild' },
          { text: '- Android Studio Update', link: '/Maintenance/UpdateComputerBuild' },
        ],
      },
      {
        text: '8) Getting Help',
        items: [
          { text: 'Where can I get help with AAPS', link: '/GettingHelp/WhereCanIGetHelp' },
          { text: 'General troubleshooting', link: '/GettingHelp/GeneralTroubleshooting' },
          { text: '- Bluetooth troubleshooting', link: '/GettingHelp/BluetoothTroubleshooting' },
          { text: 'Profile Tuning Guide', link: '/GettingHelp/ProfileTuning' },
          { text: 'Troubleshooting Android Studio', link: '/GettingHelp/TroubleshootingAndroidStudio' },
          { text: 'Troubleshooting NSClient', link: '/GettingHelp/TroubleshootingNsClient' },
          { text: 'Accessing logfiles', link: '/GettingHelp/AccessingLogFiles' },
        ],
      },
      {
        text: '9) Advanced AAPS options',
        items: [
          { text: 'Full Closed Loop', link: '/AdvancedOptions/FullClosedLoop' },
          { text: 'Dev branch', link: '/AdvancedOptions/DevBranch' },
          { text: 'Autotune', link: '/AdvancedOptions/Autotune' },
          { text: 'Insulin concentration', link: '/AdvancedOptions/InsulinConcentration' },
        ],
      },
      {
        text: '10) How to support AAPS',
        items: [
          { text: 'How to help', link: '/SupportingAaps/HowCanIHelp' },
          { text: 'Editing the docs', link: '/SupportingAaps/HowToEditTheDocs' },
          { text: 'Translating the app and docs', link: '/SupportingAaps/Translations' },
          { text: 'State of translations', link: '/SupportingAaps/StateOfTranslations' },
          { text: 'Open Humans Uploader', link: '/SupportingAaps/OpenHumans' },
        ],
      },
      {
        text: '11) Resources',
        items: [
          { text: 'Glossary', link: '/UsefulLinks/Glossary' },
          { text: 'FAQ', link: '/UsefulLinks/FAQ' },
          { text: 'General diabetes and looping resources', link: '/UsefulLinks/BackgroundReading' },
          { text: 'Dedicated Google account for AAPS (optional)', link: '/UsefulLinks/DedicatedGoogleAccountForAaps' },
          { text: 'For Clinicians (outdated)', link: '/UsefulLinks/ClinicianGuideToAaps' },
        ],
      },
    ],
    search: {
      provider: 'local',
    },
  },
})
