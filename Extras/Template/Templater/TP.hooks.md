---
key: value
tags: Status/TODO
---
// Update frontmatter after template finishes executing
<%*
tp.hooks.on_all_templates_executed(async () => {
  const file = tp.file.find_tfile(tp.file.path(true));
  await tp.app.fileManager.processFrontMatter(file, (frontmatter) => {
    frontmatter["title"] = "<% tp.file.title %>";
    frontmatter["alias"] = "";
    frontmatter["date"] = "<% tp.file.creation_date() %>";
    frontmatter["categories"] = "";
    frontmatter["tags"] = "";
  });
});
%>
// Run a command from another plugin that modifies the current file, after Templater has updated the file
<%*
tp.hooks.on_all_templates_executed(() => {
  tp.app.commands.executeCommandById("obsidian-linter:lint-file");
});
-%>
