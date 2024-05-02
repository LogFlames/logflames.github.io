import tomllib
import htmlmin

about_name = ""
about_position = ""
about_text = ""
resume_education = ""
resume_experience = ""
resume_volunteering = ""
projects_categories_filteritems = ""
projects_categories_selectitems = ""
projects = ""
posters = ""

print("Reading 'text.toml'...")

with open("text.toml", "rb") as f:
    data = tomllib.load(f)

    about_name = data["about"]["name"]
    about_position = "<br>".join(data["about"]["position"])
    about_text = data["about"]["text"]

    for education in data["resume"]["education"]:
        resume_education += f"""
        <li class="timeline-item">
              <h4 class="h4 timeline-item-title">{education["title"]}</h4>
              <span>{education["time"]}</span>
              <p class="timeline-text">
              {education["description"]}
              </p>
        </li>"""

    for experience in data["resume"]["experience"]:
        resume_experience += f"""
        <li class="timeline-item">
              <h4 class="h4 timeline-item-title">{experience["title"]}</h4>
              <span>{experience["time"]}</span>
              <p class="timeline-text">
              {experience["description"]}
              </p>
        </li>"""

    for volunteering in data["resume"]["volunteering"]:
        resume_volunteering += f"""
        <li class="timeline-item">
              <h4 class="h4 timeline-item-title">{volunteering["title"]}</h4>
              <span>{volunteering["time"]}</span>
              <p class="timeline-text">
              {volunteering["description"]}
              </p>
        </li>"""

    project_tags = set()
    for project in data["projects"]:
        for tag in project["tags"]:
            project_tags.add(tag)

    for tag in sorted(list(project_tags)):
        projects_categories_filteritems += f"""
        <li class="filter-item">
          <button data-filter-btn>{tag}</button>
        </li>"""

        projects_categories_selectitems += f"""
        <li class="select-item">
            <button data-filter-btn>{tag}</button>
        </li>"""

    for project in data["projects"]:
        projects += f"""
        <li class="project-item  active" data-filter-item data-category="{" ".join(project["tags"]).lower()}">
            <a href="{project["link"]}">
                <figure class="project-img">
                  <div class="project-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>

                  <img src="{project["img"]}" alt="{project["img-alt"]}" loading="lazy">
                </figure>

                <h3 class="project-title">{project["title"]}</h3>
                <h4 class="project-desc">{project["description"]}</h4>

                <p class="project-category">{", ".join(project["tags"])}</p>

              </a>
        </li>"""

    for poster in data["posters"]:
        posters += f"""
        <li class="poster-item  active">
              <a href="{poster["pdf"]}">

                <figure class="poster-img">
                  <div class="poster-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>

                  <img src="{poster["img"]}" alt="{poster["img-alt"]}" loading="lazy">
                </figure>

                <h3 class="poster-title">{poster["title"]}</h3>
                <h4 class="poster-desc">{poster["description"]}</h4>
              </a>
        </li>"""

print("Reading 'index.html.template'...")

with open("index.html.template", "r", encoding = "utf-8") as f:
    index = f.read() \
        .replace("<!-- ABOUT:NAME -->", about_name) \
        .replace("<!-- ABOUT:POSITION -->", about_position) \
        .replace("<!-- ABOUT:TEXT -->", about_text) \
        .replace("<!-- RESUME:EDUCATION -->", resume_education) \
        .replace("<!-- RESUME:EXPERIENCE -->", resume_experience) \
        .replace("<!-- RESUME:VOLUNTEERING -->", resume_volunteering) \
        .replace("<!-- PROJECTS:CATEGORIES:FILTERITEMS -->", projects_categories_filteritems) \
        .replace("<!-- PROJECTS:CATEGORIES:SELECTITEMS -->", projects_categories_selectitems) \
        .replace("<!-- PROJECTS:LIST -->", projects) \
        .replace("<!-- POSTERS:LIST -->", posters)

print("Writing 'index.html'...")


minified = htmlmin.minify(index, remove_empty_space=True)

with open("index.html", "w+", encoding = "utf-8") as f:
    f.write(minified)

print("Done")
