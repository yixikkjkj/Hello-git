#!/bin/sh

downloadPythonLanguage()
{
  fileName="Python-Language-Server-osx-x64.0.5.51.nupkg"
  if [ ! -f ~/$fileName ]
  then
    echo $fileName not exist
    wget -O ~/$fileName https://pvsc.azureedge.net/python-language-server-stable/$fileName
  fi
}

makeTargetDir()
{
  dirList=`ls ~/.vscode/extensions/ | grep "ms-python.python-"`
  echo $dirList
  maxVersion=(0 0 0)
  for nowDir in $dirList
  do
    versionList=(`echo ${nowDir##*ms-python.python-} | tr "." " "`)
    for idx in 0 1 2
    do
      if [ ${versionList[$idx]} -gt ${maxVersion[$idx]} ]
      then
        maxVersion[0]=${versionList[0]}
        maxVersion[1]=${versionList[1]}
        maxVersion[2]=${versionList[2]}
        break
      elif [ ${versionList[$idx]} -lt ${maxVersion[$idx]} ]
      then
        break
      fi
    done
  done
  export targetDir=".vscode/extensions/ms-python.python-${maxVersion[0]}.${maxVersion[1]}.${maxVersion[2]}/languageServer.0.5.51/"
  echo $targetDir
  return 0
}

main()
{
  downloadPythonLanguage
  makeTargetDir
  unzip -o ~/Python-Language-Server-osx-x64.0.5.51.nupkg -d ~/$targetDir
  chmod +x ~/${targetDir}Microsoft.Python.LanguageServer
  echo "this damn python languageServer updated done in ${targetDir}"
}

main
