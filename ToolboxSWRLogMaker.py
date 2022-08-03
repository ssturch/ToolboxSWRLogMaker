Module Module1
    Public OriginalToolboxFolder As String
    Public ToolboxVersion As String
    Public PathToSaveSWRLog As String

    Sub Main()

        Console.WriteLine("������� ������ ������������� Toolbox c ������� ����� ����������� ���������")
        ToolboxVersion = Console.ReadLine()

        Dim ValidPath As Boolean = False

        While Not ValidPath
            Console.WriteLine("������� �����, ���� ����� ����������� SWRLog ���� �� ���������� ������������� Toolbox")
            PathToSaveSWRLog = Console.ReadLine()
            If My.Computer.FileSystem.DirectoryExists(PathToSaveSWRLog) = True Then
                Console.WriteLine("������ ����� ����������")
                ValidPath = True
            Else
                Console.WriteLine("������ ����� �� ����������, ��������� ������������ ����� � ������� �����")

            End If
        End While

        ValidPath = False

        While Not ValidPath
            Console.WriteLine("������� ����� � ������������ Toolbox ��� ��������� ��� ���������")
            OriginalToolboxFolder = Console.ReadLine()
            If My.Computer.FileSystem.DirectoryExists(OriginalToolboxFolder) = True Then
                Console.WriteLine("������ ����� ����������")
                ValidPath = True
            Else
                Console.WriteLine("������ ����� �� ����������, ��������� ������������ ����� � ������� �����")

            End If
        End While

        Dim IsToolboxPath As Boolean = False

        While Not IsToolboxPath
            If My.Computer.FileSystem.FileExists(OriginalToolboxFolder & "\lang\English\SWBrowser.mdb") = True Or My.Computer.FileSystem.FileExists(OriginalToolboxFolder & "\lang\English\SWBrowser.sldedb") = True Then
                Console.WriteLine("������ ����� �������� ������ Toolbox")
                IsToolboxPath = True
            Else
                Console.WriteLine("������ ����� �� �������� ���������� Toolbox, ��������� ������������ ����� � ������� �����")
            End If
        End While



        My.Computer.FileSystem.WriteAllText(PathToSaveSWRLog & "\ToolboxFileList " & ToolboxVersion & ".swrlog", "***SWRLog for Toolbox***" & vbCrLf, False)

        For Each FoundFileAndPath As String In
            My.Computer.FileSystem.GetFiles(OriginalToolboxFolder, FileIO.SearchOption.SearchAllSubDirectories)
            My.Computer.FileSystem.WriteAllText(PathToSaveSWRLog & "\ToolboxFileList " & ToolboxVersion & ".swrlog", FoundFileAndPath & vbCrLf, True)
        Next

        Console.WriteLine("������ ��������� Toolbox ���������, ������� ����� ������")
        Console.ReadLine()

    End Sub

End Module
