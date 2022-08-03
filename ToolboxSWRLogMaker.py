Module Module1
    Public OriginalToolboxFolder As String
    Public ToolboxVersion As String
    Public PathToSaveSWRLog As String

    Sub Main()

        Console.WriteLine("Введите версию оригинального Toolbox c которой будет списываться структура")
        ToolboxVersion = Console.ReadLine()

        Dim ValidPath As Boolean = False

        While Not ValidPath
            Console.WriteLine("Введите папку, куда будет сохраняться SWRLog файл со структурой оригинального Toolbox")
            PathToSaveSWRLog = Console.ReadLine()
            If My.Computer.FileSystem.DirectoryExists(PathToSaveSWRLog) = True Then
                Console.WriteLine("Данная папка существует")
                ValidPath = True
            Else
                Console.WriteLine("Данная папка не существует, проверьте правильность ввода и введите снова")

            End If
        End While

        ValidPath = False

        While Not ValidPath
            Console.WriteLine("Введите папку с оригинальным Toolbox для получения его структуры")
            OriginalToolboxFolder = Console.ReadLine()
            If My.Computer.FileSystem.DirectoryExists(OriginalToolboxFolder) = True Then
                Console.WriteLine("Данная папка существует")
                ValidPath = True
            Else
                Console.WriteLine("Данная папка не существует, проверьте правильность ввода и введите снова")

            End If
        End While

        Dim IsToolboxPath As Boolean = False

        While Not IsToolboxPath
            If My.Computer.FileSystem.FileExists(OriginalToolboxFolder & "\lang\English\SWBrowser.mdb") = True Or My.Computer.FileSystem.FileExists(OriginalToolboxFolder & "\lang\English\SWBrowser.sldedb") = True Then
                Console.WriteLine("Данная папка является папкой Toolbox")
                IsToolboxPath = True
            Else
                Console.WriteLine("Данная папка не содержит компоненты Toolbox, проверьте правильность ввода и введите снова")
            End If
        End While



        My.Computer.FileSystem.WriteAllText(PathToSaveSWRLog & "\ToolboxFileList " & ToolboxVersion & ".swrlog", "***SWRLog for Toolbox***" & vbCrLf, False)

        For Each FoundFileAndPath As String In
            My.Computer.FileSystem.GetFiles(OriginalToolboxFolder, FileIO.SearchOption.SearchAllSubDirectories)
            My.Computer.FileSystem.WriteAllText(PathToSaveSWRLog & "\ToolboxFileList " & ToolboxVersion & ".swrlog", FoundFileAndPath & vbCrLf, True)
        Next

        Console.WriteLine("Запись структуры Toolbox завершена, нажмите любую кнопку")
        Console.ReadLine()

    End Sub

End Module
